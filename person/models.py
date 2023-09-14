from pydantic import BaseModel, Field

class Person(BaseModel):
    id: int = Field(default_factory=lambda: auto_id()) 
    name: str
    age: int
    
id_count = 0

def auto_id():
    global id_count
    id_count += 1
    return id_count 