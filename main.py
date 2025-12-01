from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
from uuid import uuid4

app = FastAPI(title="Person API", version="1.0.0")

# Pydantic model for Person
class Person(BaseModel):
    id: Optional[str] = None
    name: str
    age: int
    email: str

# In-memory database
persons_db: Dict[str, Person] = {}

@app.get("/")
def read_root():
    return {"message": "Person API - Use /docs for API documentation"}

@app.get("/persons")
def get_all_persons():
    """Get all persons"""
    return {"persons": list(persons_db.values())}

@app.get("/persons/{person_id}")
def get_person(person_id: str):
    """Get a specific person by ID"""
    if person_id not in persons_db:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons_db[person_id]

@app.post("/persons")
def create_person(person: Person):
    """Create a new person"""
    person_id = str(uuid4())
    person.id = person_id
    persons_db[person_id] = person
    return {"message": "Person created successfully", "person": person}

@app.put("/persons/{person_id}")
def update_person(person_id: str, person: Person):
    """Update an existing person"""
    if person_id not in persons_db:
        raise HTTPException(status_code=404, detail="Person not found")
    person.id = person_id
    persons_db[person_id] = person
    return {"message": "Person updated successfully", "person": person}

@app.delete("/persons/{person_id}")
def delete_person(person_id: str):
    """Delete a person"""
    if person_id not in persons_db:
        raise HTTPException(status_code=404, detail="Person not found")
    deleted_person = persons_db.pop(person_id)
    return {"message": "Person deleted successfully", "person": deleted_person}
