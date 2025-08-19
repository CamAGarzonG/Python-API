import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_user_cart():
    r = requests.get(f"{BASE_URL}/carts/user/2")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)

def test_delete_cart_invalid():
    r = requests.delete(f"{BASE_URL}/carts/9999")
    assert r.status_code in [404, 400]

def test_update_product():
    payload = {"title": "Updated Product", "price": 199.99}
    r = requests.put(f"{BASE_URL}/products/1", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == payload["title"]
    assert data["price"] == payload["price"]
