from fastapi import FastAPI
from app.routers import router_items

# Initialize the FastAPI app
app = FastAPI(
    title="Inventory API",
    docs_url='/'
)

# Include the router for managing items
app.include_router(router_items.router)
