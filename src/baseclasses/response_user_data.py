from src.enums.global_enums import GlobalErrorMessages


class ResponseUserData:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json["data"], list):
            for item in self.response_json["data"]:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json["data"])
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, f"{GlobalErrorMessages.WRONG_STATUS_CODE.value}\n{self}"
        else:
            assert self.response_status == status_code, f"{GlobalErrorMessages.WRONG_STATUS_CODE.value}\n{self}"
        return self

    def __str__(self):
        return f"Status code: {self.response_status}\n" \
               f"Request url: {self.response.url}\n" \
               f"Response body: {self.response_json}"
