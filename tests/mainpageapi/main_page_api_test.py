import pytest
import requests
from configuration import SERVICE_API_URL
from src.baseclasses.response_data import Response
from src.schemes.user_schemes import UserDataSchema, CreateUserSchema, UpdateUserSchema, \
    RegisterMewUserSuccessfulSchema, RegisterOrLoginUserUnsuccessfulSchema, LoginUserSuccessfulSchema
from src.schemes.resource_schemes import ResourceDataSchema


class TestAPIMainPage:
    @pytest.mark.parametrize("get_users", ["get_list_users"], indirect=True)
    def test_get_list_users(self, get_users):
        test_object = Response(get_users)
        test_object.assert_status_code([200]).validate(UserDataSchema)

    @pytest.mark.parametrize("get_users", ["get_single_user"], indirect=True)
    def test_get_single_user(self, get_users):
        test_object = Response(get_users)
        test_object.assert_status_code([200]).validate(UserDataSchema)

    @pytest.mark.parametrize("get_users", ["get_single_user_not_found"], indirect=True)
    def test_get_single_user_not_found(self, get_users):
        test_object = Response(get_users)
        test_object.assert_status_code([404]).validate_not_found()

    @pytest.mark.parametrize("get_resources", ["get_list_resource"], indirect=True)
    def test_get_list_resource(self, get_resources):
        test_object = Response(get_resources)
        test_object.assert_status_code([200]).validate(ResourceDataSchema)

    @pytest.mark.parametrize("get_resources", ["get_single_resource"], indirect=True)
    def test_get_single_resource(self, get_resources):
        test_object = Response(get_resources)
        test_object.assert_status_code([200]).validate(ResourceDataSchema)

    @pytest.mark.parametrize("get_resources", ["get_single_resource_not_found"], indirect=True)
    def test_get_single_resource_not_found(self, get_resources):
        test_object = Response(get_resources)
        test_object.assert_status_code([404]).validate_not_found()

    def test_create_new_user(self):
        user_data = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(url=f"{SERVICE_API_URL}users", data=user_data)
        test_object = Response(response)
        test_object.assert_status_code([201]).validate_user(CreateUserSchema)
        name = test_object.response_json["name"]
        job = test_object.response_json["job"]
        assert name == "morpheus", "New users name did not create"
        assert job == "leader", "New users job did not create"

    @pytest.mark.parametrize("update_new_user", ["put", "patch"], indirect=True)
    def test_update_user_put_patch(self, update_new_user):
        test_object = Response(update_new_user)
        test_object.assert_status_code([200]).validate_user(UpdateUserSchema)
        name = test_object.response_json["name"]
        job = test_object.response_json["job"]
        assert name == "morpheus", "New users name did not create"
        assert job == "zion resident", "New users job did not create"

    def test_delete_user(self):
        response = requests.delete(url=f"{SERVICE_API_URL}users/2")
        assert response.status_code == 204, "User has not been deleted"

    def test_register_new_user_successful(self):
        user_data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = requests.post(url=f"{SERVICE_API_URL}register", data=user_data)
        test_object = Response(response)
        test_object.assert_status_code([200]).validate_user(RegisterMewUserSuccessfulSchema)

    def test_register_new_user_unsuccessful(self):
        user_data = {
            "email": "sydney@fife"
        }
        response = requests.post(url=f"{SERVICE_API_URL}register", data=user_data)
        test_object = Response(response)
        test_object.assert_status_code([400]).validate_user(RegisterOrLoginUserUnsuccessfulSchema)
        registration_error_message = test_object.response_json["error"]
        assert registration_error_message == "Missing password", "Check registration error message"

    def test_login_user_successful(self):
        user_data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post(url=f"{SERVICE_API_URL}login", data=user_data)
        test_object = Response(response)
        test_object.assert_status_code([200]).validate_user(LoginUserSuccessfulSchema)

    def test_login_user_unsuccessful(self):
        user_data = {
            "email": "peter@klaven"
        }
        response = requests.post(url=f"{SERVICE_API_URL}login", data=user_data)
        test_object = Response(response)
        test_object.assert_status_code([400]).validate_user(RegisterOrLoginUserUnsuccessfulSchema)
        registration_error_message = test_object.response_json["error"]
        assert registration_error_message == "Missing password", "Check registration error message"

    def test_delayed_get_list_users(self):
        response = requests.get(url=f"{SERVICE_API_URL}users?delay=3")
        test_object = Response(response)
        test_object.assert_status_code([200]).validate(UserDataSchema)
