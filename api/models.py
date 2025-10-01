from pydantic import BaseModel

class Data(BaseModel):
    title: str
    message: str