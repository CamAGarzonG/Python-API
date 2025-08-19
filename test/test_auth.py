import requests

BASE_URL = "https://fakestoreapi.com"

def test_login_valid_user():
    payload = {"username": "mor_2314", "password": "83r5^_"}
    r = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert r.status_code in [200, 201]
    data = r.json()
    assert "token" in data

def test_login_invalid_user():
    payload = {"username": "fake_user", "password": "wrong"}
    r = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert r.status_code in [401, 400]
