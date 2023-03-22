from pydantic import BaseModel, validator
from src.enums.user_enums import UserErrors


class UserDataSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @validator("email")
    def check_that_dog_presented_in_email_address(cls, email):
        if "@" in email:
            return email
        raise ValueError(UserErrors.WRONG_EMAIL.value)
