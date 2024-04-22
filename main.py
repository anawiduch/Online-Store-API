from fastapi import FastAPI
from routers import product, order

app = FastAPI()

# Include routers for products and orders
app.include_router(product.router)
app.include_router(order.router)
