# project-15
vibe coding, python, fastapi postgres and redis

## Person REST API

A REST API built with FastAPI for managing Person objects.

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

### API Endpoints

- **GET** `/persons` - Get all persons
- **GET** `/persons/{person_id}` - Get a specific person by ID
- **POST** `/persons` - Create a new person
- **PUT** `/persons/{person_id}` - Update a person
- **DELETE** `/persons/{person_id}` - Delete a person

### Person Object Schema

```json
{
  "name": "string",
  "age": "integer",
  "email": "string"
}
```

### API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Example Usage

**Create a person:**
```bash
curl -X POST "http://localhost:8000/persons" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 30, "email": "john@example.com"}'
```

**Get all persons:**
```bash
curl "http://localhost:8000/persons"
```

**Update a person:**
```bash
curl -X PUT "http://localhost:8000/persons/{person_id}" \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "age": 28, "email": "jane@example.com"}'
```

**Delete a person:**
```bash
curl -X DELETE "http://localhost:8000/persons/{person_id}"
```
