from time import sleep
from locators.main_page_ui_locators import MainPageUILocators
import pytest

from configuration import SERVICE_URL
from pages.main_page_ui import MainPageUI
from src.baseclasses.response_data import Response


class TestMainPageUI:
    @pytest.mark.parametrize("get_users",
                             ["get_list_users", "get_single_user", "get_single_user_not_found"],
                             indirect=True)
    def test_get_list_or_single_or_not_found_users_request(self, driver, get_users):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(get_users[1])
        response_code_api, output_response_api = \
            Response(get_users[0]).response_status, Response(get_users[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"

    @pytest.mark.parametrize("get_resources",
                             ["get_list_resource", "get_single_resource", "get_single_resource_not_found"],
                             indirect=True)
    def test_get_list_or_single_or_not_found_resource_request(self, driver, get_resources):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(get_resources[1])
        response_code_api, output_response_api = \
            Response(get_resources[0]).response_status, Response(get_resources[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"

    def test_post_create_new_user(self, driver, create_new_user):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(create_new_user[1])
        response_code_api, output_response_api = \
            Response(create_new_user[0]).response_status, Response(create_new_user[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response["job"] == output_response_api["job"], \
            "Response body 'job' key of API request does not match with UI result"
        assert output_response["name"] == output_response_api["name"], \
            "Response body 'name' key of API request does not match with UI result"

    @pytest.mark.parametrize("update_new_user", ["put", "patch"], indirect=True)
    def test_put_patch_update_user(self, driver, update_new_user):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(update_new_user[1])
        response_code_api, output_response_api = \
            Response(update_new_user[0]).response_status, Response(update_new_user[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response["job"] == output_response_api["job"], \
            "Response body 'job' key of API request does not match with UI result"
        assert output_response["name"] == output_response_api["name"], \
            "Response body 'name' key of API request does not match with UI result"

    def test_delete_user(self, driver, delete_user):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code = main_page_ui.send_request(delete_user[1])
        assert response_code == 204, "Status code of API request does not match with UI result"

    def test_post_register_new_user_successful(self, driver, register_user_successful):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(register_user_successful[1])
        response_code_api, output_response_api = \
            Response(register_user_successful[0]).response_status, Response(register_user_successful[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"

    def test_post_register_new_user_unsuccessful(self, driver, register_user_unsuccessful):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(register_user_unsuccessful[1])
        response_code_api, output_response_api = \
            Response(register_user_unsuccessful[0]).response_status, Response(register_user_unsuccessful[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"

    def test_post_login_successful(self, driver, login_successful):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(login_successful[1])
        response_code_api, output_response_api = \
            Response(login_successful[0]).response_status, Response(login_successful[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"

    def test_post_login_unsuccessful(self, driver, login_unsuccessful):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(login_unsuccessful[1])
        response_code_api, output_response_api = \
            Response(login_unsuccessful[0]).response_status, Response(login_unsuccessful[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"

    def test_get_delayed_response(self, driver, get_delayed_response):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(get_delayed_response[1])
        response_code_api, output_response_api = \
            Response(get_delayed_response[0]).response_status, Response(get_delayed_response[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"
