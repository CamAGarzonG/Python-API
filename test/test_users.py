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
    # producto numero 11
    r = requests.post(f"{BASE_URL}/users", json=payload)
    assert r.status_code in [200, 201]
    data = r.json()
    print(data)
    assert "id" in data
    assert isinstance(data["id"], int)

def test_create_user_invalid_payload():
    # Este retorna un 200, pero esta mal por que no hay ningun body. La API retorna un status code erroneo
    r = requests.post(f"{BASE_URL}/users", json={})
    assert r.status_code in [400, 500]
