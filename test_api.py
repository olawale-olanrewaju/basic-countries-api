import requests
import json

base_url = "http://127.0.0.1:8000/countries"
headers = {"Content-Type":"application/json"}
payload = {"name": "Nigeria", "capital": "Lagos", "area": 1010490}


def test_get_countries_api():
    response = requests.get(base_url)

    # print(response.json())
    # print(response.headers)
    # print(response.text) # returns response body as string
    # print(json.loads(response.text)) # Same as response.json()

    assert response.status_code == 200
    assert len(response.json()) == 3
    # assert response.json()

    # for country in response.json():
    #     for k, v in country.items():
    #         print(f"{k} and {v}\n")

    for country in response.json():
        assert "name" in country.keys()
        assert "id" in country.keys()
        assert "capital" in country.keys()
        assert country["name"] is not None


def test_post_countries_api():

    response = requests.post(url=base_url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 201
