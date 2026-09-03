# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field
from typing import List, Optional

class Product(BaseModel):
    id: str = Field(alias="_id")
    name: str
    brand: str
    category: str
    price: float
    rating: float
    review_count: int
    quantity: int
    keywords: List[str]
    description: str

    model_config = {
        "populate_by_name": True
    }
