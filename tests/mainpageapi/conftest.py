import pytest
import requests
from configuration import SERVICE_API_URL


@pytest.fixture
def get_users(request):
    if request.param == "get_list_users":
        response = requests.get(url=f"{SERVICE_API_URL}users?page=2")
        return response
    elif request.param == "get_single_user":
        response = requests.get(url=f"{SERVICE_API_URL}users/2")
        return response
    elif request.param == "get_single_user_not_found":
        response = requests.get(url=f"{SERVICE_API_URL}users/23")
        return response


@pytest.fixture
def get_resources(request):
    if request.param == "get_list_resource":
        response = requests.get(url=f"{SERVICE_API_URL}unknown")
        return response
    elif request.param == "get_single_resource":
        response = requests.get(url=f"{SERVICE_API_URL}unknown/2")
        return response
    elif request.param == "get_single_resource_not_found":
        response = requests.get(url=f"{SERVICE_API_URL}unknown/23")
        return response
