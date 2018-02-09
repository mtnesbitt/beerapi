import beerapi

def test_route_gives_hello_world():
    beerapi.app.testing = True
    app = beerapi.app.test_client()

    result = app.get('/')
    assert b"Hello World" in result.data
