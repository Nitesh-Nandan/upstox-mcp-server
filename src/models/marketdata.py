from pydantic import BaseModel, Field
from typing import Dict


class QuoteData(BaseModel):
    """Model for individual quote data"""
    instrument_token: str = Field(..., description="Instrument token")
    last_price: float = Field(..., description="Last traded price")
    previous_day_closing_price: float = Field(..., description="Previous day closing price")
    ltq: int = Field(..., description="Last traded quantity")
    volume: int = Field(..., description="Total volume traded")

    @classmethod
    def from_market_quote_data(cls, data: Dict):
        for key, value in data.items():
            return QuoteData(
                instrument_token=value["instrument_token"],
                last_price=value["last_price"],
                previous_day_closing_price=value["cp"],
                ltq=value["ltq"],
                volume=value["volume"]
            )

class OHLCData(BaseModel):
    """Model for OHLC data"""
    instrument_token: str = Field(..., description="Instrument token")
    open: float = Field(..., description="Open price")
    high: float = Field(..., description="High price")
    low: float = Field(..., description="Low price")
    close: float = Field(..., description="Close price")
    volume: int = Field(..., description="Total volume traded")

    
class OHLCResponse(BaseModel):
    """Model for OHLC response"""
    instrument_token: str = Field(..., description="Instrument token")
    last_price: float = Field(..., description="Last price")
    prev_ohlc: OHLCData = Field(..., description="Previous day OHLC data")
    live_ohlc: OHLCData = Field(..., description="Live OHLC data")

    @classmethod
    def from_api_response(cls, data: Dict):
        for key, value in data.items():
            return OHLCResponse(
                instrument_token=value["instrument_token"],
                last_price=value["last_price"],
                prev_ohlc=OHLCData(**value["prev_ohlc"]),
                live_ohlc=OHLCData(**value["live_ohlc"])
            )