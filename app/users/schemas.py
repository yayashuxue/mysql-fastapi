from datetime import datetime
from pydantic import BaseModel, Field

class UserBalances(BaseModel):
    address: str = Field(..., description="address", max_length=255)
    onChainBal: str = Field(..., description="onChainBal", max_length=255)
    localBal: str = Field(..., description="localBal", max_length=255)
    inPlay: str = Field(..., description="inPlay", max_length=255)

class UserCreate(UserBalances):
    created: datetime = Field(description="created")