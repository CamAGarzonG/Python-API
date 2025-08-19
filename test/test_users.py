import requests
from faker import Faker

BASE_URL = "https://fakestoreapi.com"
fake = Faker()

def test_create_user():
    payload = {
        "email": fake.email(),
        "username": fake.user_name(),
        "password": "Password123"
    }

    r = requests.post(f"{BASE_URL}/users", json=payload)
    assert r.status_code in [200, 201]
    data = r.json()
    print(data)
    assert "id" in data
    assert data["username"] == payload["username"]

def test_create_user_invalid_payload():
    r = requests.post(f"{BASE_URL}/users", json={})
    assert r.status_code in [400, 500]
