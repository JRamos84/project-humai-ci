import pytest
from application.api_client import APIClient
from requests.exceptions import HTTPError


@pytest.fixture
def api_client():
    """Fixture para inicializar el cliente de la API."""
    return APIClient(baseUrl="https://jsonplaceholder.typicode.com")


def test_get_users(api_client):
    users = api_client.get_users()
    assert isinstance(users, list)
    assert len(users) > 0
    assert "name" in users[0]