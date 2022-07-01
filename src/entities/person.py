from pydantic import BaseModel


class Person(BaseModel):
    name: str
    surname: str
    salary: float

