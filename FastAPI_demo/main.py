from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

products = [Product(id=1, name="Laptop", description="High-performance laptop", quantity=10, price=999.99),
           Product(id=2, name="Smartphone", description="Latest model smartphone", quantity=20, price=499.99),
           Product(id=3, name="Headphones", description="Noise-cancelling headphones", quantity=15, price=199.99),
           Product(id=4, name="Smartwatch", description="Feature-rich smartwatch", quantity=25, price=299.99),
           Product(id=5, name="Tablet", description="Lightweight tablet", quantity=30, price=399.99)]

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{id}")
def get_product_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Products Not Found"

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products")
def update_product(id: int, updated_product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return "Product updated successfully"
    return "Product Not Found"