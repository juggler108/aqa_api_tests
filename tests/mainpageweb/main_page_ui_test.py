from time import sleep

import pytest

from configuration import SERVICE_URL
from pages.main_page_ui import MainPageUI
from src.baseclasses.response_data import Response


class TestMainPageUI:
    @pytest.mark.parametrize("get_users",
                             ["get_list_users", "get_single_user", "get_single_user_not_found"],
                             indirect=True)
    def test_check_get_list_or_single_or_not_found_users_request(self, driver, get_users):
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
    def test_check_get_users_not_found_request(self, driver, get_resources):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
        response_code, output_response = main_page_ui.send_request(get_resources[1])
        response_code_api, output_response_api = \
            Response(get_resources[0]).response_status, Response(get_resources[0]).response_json
        assert response_code == response_code_api, "Status code of API request does not match with UI result"
        assert output_response == output_response_api, "Response body of API request does not match with UI result"


