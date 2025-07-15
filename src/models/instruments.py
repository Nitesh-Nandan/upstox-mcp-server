from pydantic import BaseModel

class Instrument(BaseModel):
    """Represents a trading instrument with symbol and key."""
    tradingsymbol: str
    instrumentKey: str
