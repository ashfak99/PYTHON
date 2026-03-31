from pydantic import BaseModel

class item(BaseModel):
    Name : str
    Price : int =0
    Count : int =0