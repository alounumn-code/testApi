
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Product Card API")

# Allow requests from the React development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

products = [
    {
        "id": 1,
        "name": "Mechanical Keyboard",
        "price": 79.99,
        "category": "Accessories",
        "image": "https://placehold.co/600x400?text=Keyboard",
        "description": "A mechanical keyboard for programming and daily work."
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "price": 39.50,
        "category": "Accessories",
        "image": "https://placehold.co/600x400?text=Mouse",
        "description": "A comfortable wireless mouse for office work."
    },
    {
        "id": 3,
        "name": "Developer Laptop",
        "price": 899.00,
        "category": "Computers",
        "image": "https://placehold.co/600x400?text=Laptop",
        "description": "A laptop for software development and multitasking."
    },
]


@app.get("/api/products")
def get_products():
    return products


@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )