from __future__ import annotations

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None # optional