import json
from json import JSONDecodeError
from time import sleep

from locators.main_page_ui_locators import MainPageUILocators
from pages.base_page import BasePage


class MainPageUI(BasePage):
    locators = MainPageUILocators()

    def send_request(self, request_name):
        response_content = {
            "response_code": self.locators.RESPONSE_CODE,
            "output_response": self.locators.OUTPUT_RESPONSE
        }
        request_names = {
            "users": {
                "data_key": self.locators.LIST_USERS_ENDPOINT
            },
            "users_single": {
                "data_key": self.locators.SINGLE_USER_ENDPOINT
            },
            "users_not_found": {
                "data_key": self.locators.SINGLE_USER_NOT_FOUND_ENDPOINT
            },
            "unknown": {
                "data_key": self.locators.LIST_RESOURCE_ENDPOINT
            },
            "unknown_single": {
                "data_key": self.locators.SINGLE_RESOURCE_ENDPOINT
            },
            "unknown_single_not_found": {
                "data_key": self.locators.SINGLE_RESOURCE_NOT_FOUND_ENDPOINT
            },
            "post": {
                "data_key": self.locators.CREATE_USER_ENDPOINT
            },
            "put": {
                "data_key": self.locators.UPDATE_PUT_USER_ENDPOINT
            },
            "patch": {
                "data_key": self.locators.UPDATE_PATCH_USER_ENDPOINT
            },
            "delete": {
                "data_key": self.locators.DELETE_USER_ENDPOINT
            },
            "register_successful": {
                "data_key": self.locators.REGISTER_SUCCESSFUL_USER_ENDPOINT
            },
            "register_unsuccessful": {
                "data_key": self.locators.REGISTER_UNSUCCESSFUL_USER_ENDPOINT
            },
            "login_successful": {
                "data_key": self.locators.LOGIN_SUCCESSFUL_USER_ENDPOINT
            },
            "login_unsuccessful": {
                "data_key": self.locators.LOGIN_UNSUCCESSFUL_USER_ENDPOINT
            },
            "delayed_response": {
                "data_key": self.locators.DELAYED_RESPONSE_LIST_USERS_ENDPOINT
            }
        }
        self.element_is_visible(request_names[request_name]["data_key"]).click()
        sleep(0.5)
        self.element_is_present(MainPageUILocators.DELAYED_ELEMENT)
        response_code = int(self.element_is_present(response_content["response_code"]).text)
        try:
            output_response = json.loads(self.element_is_present(response_content["output_response"]).text)
            return response_code, output_response
        except JSONDecodeError:
            return response_code
