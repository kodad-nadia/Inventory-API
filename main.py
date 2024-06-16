from fastapi import FastAPI
import routers.router_items 

# Initialize the FastAPI app
app = FastAPI(
    title="Inventory API",
    docs_url='/'
)

# Include the router for managing items
app.include_router(routers.router_items.router)











