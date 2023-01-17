from change_calculator import percentage_change


def test_should_status_code_ok(client):
        name = "Reinger Inc",
        response = client.get(f"/detail/{name}")
        assert response.status_code == 200


def test_should_display_all_company_data(client):
    company = {"name": "Reinger Inc",
               "sector": "Services",
               "siren": 135694027,
               "results": [
                           {
                            "ca": 2077357,
                            "margin": 497351,
                            "ebitda": 65952,
                            "loss": 858474,
                            "year": 2017
                            },
                            {
                            "ca": 432070,
                            "margin": 427778,
                            "ebitda": 290433,
                            "loss": 8023406,
                            "year": 2016
                            }
                           ]}
    response = client.get(f"/detail/{company['name']}")
    assert (company['sector']) in response.data.decode()
    assert str(company['siren']) in response.data.decode()
    assert str(company['results'][0]['ca']) in response.data.decode()
    assert str(company['results'][0]['margin']) in response.data.decode()
    assert str(company['results'][0]['ebitda']) in response.data.decode()
    assert str(company['results'][0]['loss']) in response.data.decode()
    assert str(company['results'][0]['year']) in response.data.decode()
    assert str(company['results'][1]['ca']) in response.data.decode()
    assert str(company['results'][1]['margin']) in response.data.decode()
    assert str(company['results'][1]['ebitda']) in response.data.decode()
    assert str(company['results'][1]['loss']) in response.data.decode()
    assert str(company['results'][1]['year']) in response.data.decode()


def test_evolution_board(client):
    company = {"name": "Reinger Inc",
               "sector": "Services",
               "siren": 135694027,
               "results": [
                           {
                            "ca": 2077357,
                            "margin": 497351,
                            "ebitda": 65952,
                            "loss": 858474,
                            "year": 2017
                            },
                            {
                            "ca": 432070,
                            "margin": 427778,
                            "ebitda": 290433,
                            "loss": 8023406,
                            "year": 2016
                            }
                           ]}
    response = client.get(f"/detail/{company['name']}")
    assert str(percentage_change(company['results'][0]['ca'],
                                 company['results'][1]['ca'])) in response.data.decode()
    assert str(percentage_change(company['results'][0]['margin'],
                                 company['results'][1]['margin'])) in response.data.decode()
    assert str(percentage_change(company['results'][0]['ebitda'],
                                 company['results'][1]['ebitda'])) in response.data.decode()
    assert str(percentage_change(company['results'][0]['loss'],
                                 company['results'][1]['loss'])) in response.data.decode()
