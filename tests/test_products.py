from app.models import Product


def test_create_product(client):
    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 50000,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Laptop"
    assert data["price"] == 50000
    assert data["id"] is not None


def test_get_products(client, db):
    product = Product(
        name="Laptop",
        price=50000,
    )

    db.add(product)
    db.commit()

    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Laptop"
    assert data[0]["price"] == 50000


def test_create_product_invalid_price(client):
    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": "hello",
        },
    )

    assert response.status_code == 422

    def test_create_product_missing_price(client):
        response = client.post(
            "/products",
            json={
                "name": "Laptop",
            },
        )

    assert response.status_code == 422
