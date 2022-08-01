# transactions_response.py

from datetime import datetime
from pydantic import BaseModel, validator, Field
    
    
class TransactionsResponse(BaseModel):
    hash: str
    from_address: str = Field(alias="fromAddress")
    to_address: str = Field(alias="toAddress")
    block_number: str = Field(alias="blockNumber")
    utc_timestamp: datetime = Field(alias="executedAt")
    gas_cost_in_gwei: float = Field(alias="gasUsed")
    eth_price: float = Field(alias="gasCostInDollars")

    class Config:
        allow_population_by_field_name = True
    
    @validator("utc_timestamp", pre=False)
    def datetime_to_str(cls, value):
        if value:
            return str(value)