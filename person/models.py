from pydantic import BaseModel
from typing import Union


class Person(BaseModel):
    id:  Union[int, None] = None
    name: str
    
    
    
id_count = 0
def auto_id():
    global id_count
    id_count += 1
    return id_count 