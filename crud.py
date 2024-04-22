from sqlalchemy.orm import Session
from models import Product, Order

def get_products(db: Session):
    return db.query(Product).all()

def create_product(db: Session, name: str, description: str, price: float):
    product = Product(name=name, description=description, price=price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(db: Session, product_id: int, new_price: float, new_description: str):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        product.price = new_price
        product.description = new_description
        db.commit()
        return product
    return None

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return True
    return False
