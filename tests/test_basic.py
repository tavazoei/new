from app.models import Product


def test_database(db):
    product = Product(
        name="Test Laptop",
        price=100,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    assert product.id is not None
    assert product.name == "Test Laptop"
    assert product.price == 100
