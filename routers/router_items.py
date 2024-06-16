from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid

router = APIRouter(tags=["Items"])

# Example data (simulating a database)
items = [
    {"id": str(uuid.uuid4()), "name": "Item 1", "description": "Description of Item 1"},
    {"id": str(uuid.uuid4()), "name": "Item 2", "description": "Description of Item 2"},
    {"id": str(uuid.uuid4()), "name": "Item 3", "description": "Description of Item 3"}
]

# Pydantic model for input validation
class ItemBase(BaseModel):
    name: str
    description: str

# Pydantic model for response
class Item(ItemBase):
    id: str

# Endpoint to list all items
@router.get('/items', response_model=list[Item])
async def list_items():
    return items

# Endpoint to create a new item
@router.post('/items', response_model=Item)
async def create_item(item: ItemBase):
    new_item = {"id": str(uuid.uuid4()), **item.dict()}
    items.append(new_item)
    return new_item

# Endpoint to get item by ID
@router.get('/items/{item_id}', response_model=Item)
async def get_item(item_id: str):
    for item in items:
        if item['id'] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Endpoint to update item by ID
@router.put('/items/{item_id}', response_model=Item)
async def update_item(item_id: str, item: ItemBase):
    for i, existing_item in enumerate(items):
        if existing_item['id'] == item_id:
            updated_item = {"id": item_id, **item.dict()}
            items[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Endpoint to delete item by ID
@router.delete('/items/{item_id}', status_code=204)
async def delete_item(item_id: str):
    for i, item in enumerate(items):
        if item['id'] == item_id:
            del items[i]
            return
    raise HTTPException(status_code=404, detail="Item not found")
