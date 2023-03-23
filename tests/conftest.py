import pytest
import requests
from configuration import SERVICE_API_URL


@pytest.fixture
def get_users(request):
    if request.param == "get_list_users":
        return requests.get(url=f"{SERVICE_API_URL}users?page=2"), "users"
    elif request.param == "get_single_user":
        return requests.get(url=f"{SERVICE_API_URL}users/2"), "users_single"
    elif request.param == "get_single_user_not_found":
        return requests.get(url=f"{SERVICE_API_URL}users/23"), "users_not_found"


@pytest.fixture
def get_resources(request):
    if request.param == "get_list_resource":
        return requests.get(url=f"{SERVICE_API_URL}unknown"), "unknown"
    elif request.param == "get_single_resource":
        return requests.get(url=f"{SERVICE_API_URL}unknown/2"), "unknown_single"
    elif request.param == "get_single_resource_not_found":
        return requests.get(url=f"{SERVICE_API_URL}unknown/23"), "unknown_single_not_found"


@pytest.fixture
def update_new_user(request):
    user_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    if request.param == "put":
        return requests.put(url=f"{SERVICE_API_URL}users/2", data=user_data)
    return requests.patch(url=f"{SERVICE_API_URL}users/2", data=user_data)
