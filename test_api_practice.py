import requests


def test_get_api_request():
    response = requests.get("https://automationexercise.com/api/productsList")

    assert response.status_code == 200