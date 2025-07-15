import pandas as pd
from pydantic import BaseModel
import csv
from pathlib import Path
from typing import Dict


class Instrument(BaseModel):
    """Represents a trading instrument with symbol and key."""
    tradingsymbol: str
    instrumentKey: str


class InstrumentCache:
    """
    Caches and provides lookup for Upstox trading instruments.
    
    Downloads instrument data from Upstox API, filters out complex symbols,
    and provides fast lookup between trading symbols and instrument keys.
    """
    
    file_path = Path("instruments.csv")
    INSTRUMENTS_URL = "https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz"

    def __init__(self):
        """Initialize cache and load instruments from file or download fresh data."""
        self.symbol_dict: Dict[str, str] = {}
        self.instrument_dict: Dict[str, str] = {}
        self.load_instruments()

    def _is_alphanumeric(self, text: str) -> bool:
        """Check if text contains both letters and digits (complex instruments)."""
        return isinstance(text, str) and text.isalnum() and any(c.isalpha() for c in text) and any(c.isdigit() for c in text)

    def refresh_instruments(self) -> None:
        """Download fresh instrument data from Upstox and save to CSV."""
        df = pd.read_csv(self.INSTRUMENTS_URL, compression="gzip")
        
        # Select relevant columns and filter out complex symbols
        df = df[["instrument_key", "tradingsymbol", "name", "exchange"]]
        df = df[~df['tradingsymbol'].apply(self._is_alphanumeric)]
        
        df.to_csv(self.file_path, index=False, header=True)

    def load_instruments(self) -> None:
        """Load instruments from CSV file, downloading if file doesn't exist."""
        if not self.file_path.exists():
            self.refresh_instruments()

        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Build lookup dictionaries
                instrument_key = row["instrument_key"].strip().upper()
                trading_symbol = row["tradingsymbol"].strip()
                exchange = row["exchange"].strip()
                
                self.instrument_dict[instrument_key] = trading_symbol
                symbol_key = f"{exchange}|{trading_symbol}".upper()
                self.symbol_dict[symbol_key] = instrument_key

    def get_symbol(self, instrument_key: str) -> Instrument:
        """
        Get trading symbol from instrument key.
        
        Args:
            instrument_key: The instrument key (e.g., 'NSE_EQ|INE040A01034')
            
        Returns:
            Instrument object with trading symbol and key
            
        Raises:
            ValueError: If instrument key not found
        """
        key = instrument_key.strip().upper()
        if key not in self.instrument_dict:
            raise ValueError(f"Invalid instrument key: {key}")

        trading_symbol = self.instrument_dict[key]
        if '|' in key:
            exchange = key.split("|")[0]
            trading_symbol = f"{exchange}|{trading_symbol}"
        
        return Instrument(tradingsymbol=trading_symbol, instrumentKey=key)

    def get_instrument(self, symbol: str, exchange: str = "NSE_EQ") -> Instrument:
        """
        Get instrument key from trading symbol.
        
        Args:
            symbol: Trading symbol (e.g., 'HDFCBANK')
            exchange: Exchange code (default: 'NSE_EQ')
            
        Returns:
            Instrument object with trading symbol and key
            
        Raises:
            ValueError: If symbol not found
        """
        full_symbol = f"{exchange.strip()}|{symbol.strip()}".upper()
        if full_symbol not in self.symbol_dict:
            raise ValueError(f"Invalid symbol: {full_symbol}")

        return Instrument(
            tradingsymbol=full_symbol,
            instrumentKey=self.symbol_dict[full_symbol]
        )

instrumentCache = InstrumentCache()

if __name__ == "__main__":
    cache = InstrumentCache()
    print(cache.get_instrument('HDFCBANK'))
    print(cache.get_symbol('NSE_EQ|INE040A01034'))
