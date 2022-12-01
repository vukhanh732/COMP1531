import json
import requests

BASE_URL = 'http://127.0.0.1:7777'

def test_system():
    # Get empty
    response = requests.get(f"{BASE_URL}/names").json()
    assert response == {'names': []}

    requests.post(f"{BASE_URL}/names/add", json={ 'names' : 'Asus' })
    requests.post(f"{BASE_URL}/names/add", json={ 'names' : 'Acer' })
    response_2 = requests.get(f"{BASE_URL}/names").json()
    assert response_2 == {'names': ['Asus', 'Acer']}

    requests.delete(f"{BASE_URL}/names/remove", json={ 'names' : 'Acer' })
    response_3 = requests.get(f"{BASE_URL}/names").json()
    assert response_3 == {'names': ['Asus']}
