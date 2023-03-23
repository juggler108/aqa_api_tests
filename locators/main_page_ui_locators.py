from selenium.webdriver.common.by import By


class MainPageUILocators:
    LIST_USERS_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='users']")
    SINGLE_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='users-single']")
    SINGLE_USER_NOT_FOUND_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='users-single-not-found']")
    LIST_RESOURCE_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='unknown']")
    SINGLE_RESOURCE_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='unknown-single']")
    SINGLE_RESOURCE_NOT_FOUND_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='unknown-single-not-found']")
    CREATE_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='post']")
    UPDATE_PUT_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='put']")
    UPDATE_PATCH_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='patch']")
    DELETE_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='delete']")
    REGISTER_SUCCESSFUL_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='register-successful']")
    REGISTER_UNSUCCESSFUL_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='register-unsuccessful']")
    LOGIN_SUCCESSFUL_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='login-successful']")
    LOGIN_UNSUCCESSFUL_USER_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='login-unsuccessful']")
    DELAYED_RESPONSE_LIST_USERS_ENDPOINT = (By.CSS_SELECTOR, "li[data-id='delay']")
