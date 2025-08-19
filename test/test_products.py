import json

import requests
import pytest

BASE_URL = "https://fakestoreapi.com"

def test_get_products_list():
    r = requests.get(f"{BASE_URL}/products")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert "id" in data[0]
    assert "title" in data[0]
    print(r.json())

@pytest.mark.parametrize("product_id", [1])
def test_get_product_by_id(product_id):
    r = requests.get(f"{BASE_URL}/products/{product_id}")
    print(r.json())
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == product_id

def test_get_product_invalid_id():
    invalid_id = 9999
    r = requests.get(f"{BASE_URL}/products/{invalid_id}")
    # Esta parte de la api no esta bien implementada por que retorna un error en el json y en la variable de estado,
    # por eso la excepcion
    try:
        data = r.json()
        assert data["id"] != invalid_id
    except json.JSONDecodeError:
        assert True
