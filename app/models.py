from pydantic import BaseModel
from typing import List

class Client(BaseModel):
    name: str
    contact: str
    lang: str = "en"

class Item(BaseModel):
    sku: str
    qty: int
    unit_cost: float
    margin_pct: float

class QuoteRequest(BaseModel):
    client: Client
    currency: str
    items: List[Item]
    delivery_terms: str
    notes: str | None = None
