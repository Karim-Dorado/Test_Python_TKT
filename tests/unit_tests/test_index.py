def test_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_first_table_raw(client):
    response = client.get('/')
    assert ("Company") in response.data.decode()
    assert ("Sector") in response.data.decode()
    assert ("Siren") in response.data.decode()


def test_table_data(client):
    response = client.get("/")

    company = {"name": "Reinger Inc",
               "sector": "Services",
               "siren": 135694027}

    assert (company['name']) in response.data.decode()
    assert (company['sector']) in response.data.decode()
    assert str(company['siren']) in response.data.decode()
