from configuration import SERVICE_URL
from pages.main_page_ui import MainPageUI


class TestMainPageUI:
    def test_check_get_list_users_request(self, driver):
        main_page_ui = MainPageUI(driver, SERVICE_URL)
        main_page_ui.open()
