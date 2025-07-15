from pydantic import BaseModel
from enum import Enum

class Exchange(str, Enum):
    """Exchange codes for trading instruments"""
    NSE_EQ = "NSE_EQ"
    BSE_EQ = "BSE_EQ"
    MCX_FO = "MCX_FO"
    NCD_FO = "NCD_FO"
    
