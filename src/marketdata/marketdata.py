import os
from typing import Union, List, Dict

import requests
from dotenv import load_dotenv

from models import Instrument, QuoteData

load_dotenv()


def getHeaders():
    access_token = os.getenv("UPSTOX_ACCESS_TOKEN")
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }


def _single_last_traded_price(instrument: Instrument) -> Union[str, QuoteData]:
    url = f"https://api.upstox.com/v3/market-quote/ltp?instrument_key={instrument.instrumentKey}"
    response = requests.get(url, headers=getHeaders())

    # Handle API errors
    if response.status_code != 200:
        error_msg = "Unknown API error"
        try:
            error_msg = response.json().get('message', error_msg)
        except:
            pass
        return f"API Error ({response.status_code}): {error_msg} for {instrument.tradingsymbol}"

    # Parse response data
    response_data = response.json()
    if not response_data.get('data'):
        return f"No data found for {instrument.tradingsymbol}"

    return QuoteData.from_market_quote_data(response_data['data'])


def get_last_traded_price(instrument: Union[Instrument, List[Instrument]]) -> Dict[str, Union[str, QuoteData]]:
    if isinstance(instrument, list):
        return {i.tradingsymbol: _single_last_traded_price(i) for i in instrument}
    else:
        return {instrument.tradingsymbol: _single_last_traded_price(instrument)}


if __name__ == "__main__":
    result = get_last_traded_price([
        Instrument(tradingsymbol="NSE_EQ|HDFCBANK", instrumentKey="NSE_EQ|INE040A01034"),
        Instrument(tradingsymbol="NSE_EQ|ICICIBANK", instrumentKey="NSE_EQ|INE090A01021"),
        Instrument(tradingsymbol="NSE_EQ|NOT", instrumentKey="NSE_EQ|NOTIED"),
    ])
    print(result)
