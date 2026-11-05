from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.auth import router as auth_router
from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate, ProductResponse

app = FastAPI()
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Product API is running on new "}


@app.post("/products", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    db_product = Product(
        name=product.name,
        price=product.price,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@app.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
