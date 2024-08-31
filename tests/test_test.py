from conftest import client


def test_request():
    response = client.post("/calculate", json={
        "date": "31.01.2021",
        "periods": 1,
        "amount": 10000,
        "rate": 1
    })

    assert response.status_code == 200
