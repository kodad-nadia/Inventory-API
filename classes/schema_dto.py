from pydantic import BaseModel

# Base class for shared attributes
class ItemBase(BaseModel):
    name: str
    description: str

# Model for creating a new item
class ItemCreate(ItemBase):
    pass

# Model for reading an item with ID
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
