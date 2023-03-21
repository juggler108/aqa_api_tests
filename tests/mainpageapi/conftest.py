import pytest
import requests
from configuration import SERVICE_API_URL


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_API_URL)
    return response
