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
def create_new_user():
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    return requests.post(url=f"{SERVICE_API_URL}users", data=user_data), "post"


@pytest.fixture
def update_new_user(request):
    user_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    if request.param == "put":
        return requests.put(url=f"{SERVICE_API_URL}users/2", data=user_data), "put"
    elif request.param == "patch":
        return requests.patch(url=f"{SERVICE_API_URL}users/2", data=user_data), "patch"


@pytest.fixture
def delete_user():
    return requests.delete(url=f"{SERVICE_API_URL}users/2"), "delete"


@pytest.fixture
def register_user_successful():
    user_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    return requests.post(url=f"{SERVICE_API_URL}register", data=user_data), "register_successful"


@pytest.fixture
def register_user_unsuccessful():
    user_data = {
        "email": "sydney@fife"
    }
    return requests.post(url=f"{SERVICE_API_URL}register", data=user_data), "register_unsuccessful"


@pytest.fixture
def login_successful():
    user_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    return requests.post(url=f"{SERVICE_API_URL}login", data=user_data), "login_successful"


@pytest.fixture
def login_unsuccessful():
    user_data = {
        "email": "peter@klaven"
    }
    return requests.post(url=f"{SERVICE_API_URL}login", data=user_data), "login_unsuccessful"


@pytest.fixture
def get_delayed_response():
    return requests.get(url=f"{SERVICE_API_URL}users?delay=3"), "delayed_response"
