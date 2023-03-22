from pydantic import BaseModel


class ResourceDataSchema(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str
