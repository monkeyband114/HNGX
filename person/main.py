from fastapi import FastAPI, HTTPException
import json
from  models import Person
app = FastAPI()


def read_db():
    with open("db.json") as f:
        return json.load(f)

# function to write to db.json
def write_db(db):
    with open("db.json", "w") as f:
        json.dump(db, f)
        
@app.post("/api")
async def create_person(person: Person):
    db = read_db()
    db["persons"].append(person.model_dump()) 
    write_db(db)
    return {"id": len(db["persons"])}

@app.get("/api/{id}") 
async def get_person(id: int):
    db = read_db()
    if id > len(db["persons"]): 
        raise HTTPException(404) 
    return db["persons"][id-1]



@app.put("/api/{id}")
async def update_person(id: int, person: Person):
  db = read_db()
  if id > len(db["persons"]):
    raise HTTPException(404)
  
  db["persons"][id-1].update(person.model_dump())
  
  write_db(db)
  
  return {"success": True}



@app.delete("/api/{id}")
async def delete_person(id: int):
  db = read_db()
  
  if id > len(db["persons"]): 
    raise HTTPException(404)
  
  db["persons"].pop(id-1)
  write_db(db)
  return {"deleted": True}

# Other CRUD routes