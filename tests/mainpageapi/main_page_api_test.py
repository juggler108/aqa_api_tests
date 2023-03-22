import pytest
from src.baseclasses.response_data import ResponseData
from src.schemes.user_schemes import UserDataSchema
from src.schemes.resource_schemes import ResourceDataSchema


class TestAPIMainPage:
    @pytest.mark.parametrize("get_users", ["get_list_users"], indirect=True)
    def test_get_list_users(self, get_users):
        test_object = ResponseData(get_users)
        test_object.assert_status_code([200]).validate(UserDataSchema)

    @pytest.mark.parametrize("get_users", ["get_single_user"], indirect=True)
    def test_get_single_user(self, get_users):
        test_object = ResponseData(get_users)
        test_object.assert_status_code([200]).validate(UserDataSchema)

    @pytest.mark.parametrize("get_users", ["get_single_user_not_found"], indirect=True)
    def test_get_single_user_not_found(self, get_users):
        test_object = ResponseData(get_users)
        test_object.assert_status_code([404]).validate_not_found()

    @pytest.mark.parametrize("get_resources", ["get_list_resource"], indirect=True)
    def test_get_list_resource(self, get_resources):
        test_object = ResponseData(get_resources)
        test_object.assert_status_code([200]).validate(ResourceDataSchema)

    @pytest.mark.parametrize("get_resources", ["get_single_resource"], indirect=True)
    def test_get_single_resource(self, get_resources):
        test_object = ResponseData(get_resources)
        test_object.assert_status_code([200]).validate(ResourceDataSchema)

    @pytest.mark.parametrize("get_resources", ["get_single_resource_not_found"], indirect=True)
    def test_get_single_resource_not_found(self, get_resources):
        test_object = ResponseData(get_resources)
        test_object.assert_status_code([404]).validate_not_found()
