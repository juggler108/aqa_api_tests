import json
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
                "data_key": self.locators.LIST_USERS_ENDPOINT,
                "content": response_content
            },
            "users_single": {
                "data_key": self.locators.SINGLE_USER_ENDPOINT,
                "content": response_content
            },
            "users_not_found": {
                "data_key": self.locators.SINGLE_USER_NOT_FOUND_ENDPOINT,
                "content": response_content
            },
            "unknown": {
                "data_key": self.locators.LIST_RESOURCE_ENDPOINT,
                "content": response_content
            },
            "unknown_single": {
                "data_key": self.locators.SINGLE_RESOURCE_ENDPOINT,
                "content": response_content
            },
            "unknown_single_not_found": {
                "data_key": self.locators.SINGLE_RESOURCE_NOT_FOUND_ENDPOINT,
                "content": response_content
            }
        }
        self.element_is_visible(request_names[request_name]["data_key"]).click()
        sleep(0.5)
        response_code = int(self.element_is_present(response_content["response_code"]).text)
        output_response = json.loads(self.element_is_present(response_content["output_response"]).text)
        return response_code, output_response
