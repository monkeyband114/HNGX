from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from  models import Person



app = FastAPI()



origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    person.id = len(db["persons"]) + 1

    db["persons"].append(person.model_dump())
    write_db(db)
    return {"id": person.id, "name": person.name}


@app.get("/api/{id}") 
async def get_person(id: int):
    db = read_db()
    person = db["persons"]
    if id > len(db["persons"]): 
        raise HTTPException(404) 
    
    return [persons for persons in person if persons["id"]==id]



@app.put("/api/{id}")
async def update_person(id: int, person: Person):
  db = read_db()
  
  if id > len(db["persons"]):
    raise HTTPException(404)
 
  data = {"id":id, "name":person.name}
  db["persons"][id-1].update(data)
  
  write_db(db)
  
  return {"id":id, "name":person.name}



@app.delete("/api/{id}")
async def delete_person(id: int):
  db = read_db()
  
  if id > len(db["persons"]): 
    raise HTTPException(404)
  
  db["persons"].pop(id-1)
  write_db(db)
  return {"deleted": True}

# Other CRUD routes