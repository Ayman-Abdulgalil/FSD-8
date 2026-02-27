# Develop RESTful APIs Using a Backend Framework

## Aim

To develop a RESTful API server using Python and Flask that performs Create, Read, Update, and Delete (CRUD) operations on student data stored in memory, and to test the API endpoints using Postman.

---

## Objective

- Set up a backend web server using the Flask framework in Python.
- Design and implement RESTful API endpoints following standard HTTP conventions.
- Manage in-memory data storage using a Python list (array) without any database.
- Understand the role of HTTP methods (GET, POST, PUT, DELETE) in REST architecture.
- Test and validate each API endpoint using the Postman tool.

---

## Theory

REST (Representational State Transfer) is an architectural style for designing networked applications. A RESTful API uses HTTP requests to perform operations on resources. Each resource is identified by a URL, and the type of operation is determined by the HTTP method used:

- GET: Retrieve data
- POST: Create new data
- PUT: Update existing data
- DELETE: Remove data

Flask is a lightweight Python web framework that makes it straightforward to build RESTful APIs. It provides routing, request handling, and JSON response utilities with minimal configuration.

---

## Steps

### 1. Install Dependencies

Ensure Python is installed on your system. Then install Flask using pip:

```
pip install flask
```

### 2. Create the Application File

Create a file named `app.py` with the following structure:

- Initialize the Flask app.
- Define an in-memory list called `students` to store student records.
- Define a `next_id` counter to auto-assign unique IDs to each student.
- Implement the following five routes:

| Route | Method | Description |
|---|---|---|
| /students | POST | Add a new student |
| /students | GET | Retrieve all students |
| /students/<id> | GET | Retrieve a single student by ID |
| /students/<id> | PUT | Update an existing student by ID |
| /students/<id> | DELETE | Delete a student by ID |

### 3. Run the Server

Start the Flask development server with:

```
python app.py
```

The server will run at `http://127.0.0.1:5000` by default.

### 4. Test Using Postman

Open Postman and create requests for each endpoint:

**Create a Student (POST)**
- Method: POST
- URL: `http://127.0.0.1:5000/students`
- Body: raw, JSON
- Sample body:
```json
{
  "name": "Alice",
  "age": 20,
  "course": "Computer Science"
}
```

**Get All Students (GET)**
- Method: GET
- URL: `http://127.0.0.1:5000/students`

**Get a Single Student (GET)**
- Method: GET
- URL: `http://127.0.0.1:5000/students/1`

**Update a Student (PUT)**
- Method: PUT
- URL: `http://127.0.0.1:5000/students/1`
- Body: raw, JSON
- Sample body:
```json
{
  "name": "Alice Smith",
  "age": 21,
  "course": "Information Technology"
}
```

**Delete a Student (DELETE)**
- Method: DELETE
- URL: `http://127.0.0.1:5000/students/1`

---

## Expected Output

- POST /students returns the created student object with a status code of 201.
- GET /students returns a list of all students with a status code of 200.
- GET /students/<id> returns the matching student or a 404 error if not found.
- PUT /students/<id> returns the updated student object with a status code of 200.
- DELETE /students/<id> returns a success message with a status code of 200.

---

## Learning Outcomes

Upon completing this experiment, students will be able to:

1. Explain the principles of REST architecture and how HTTP methods map to CRUD operations.
2. Set up and configure a Flask application to serve as a backend API server.
3. Define URL routes and handle incoming HTTP requests with appropriate response codes.
4. Work with JSON data for both receiving request payloads and sending responses.
5. Implement in-memory data management using Python lists and simulate basic database operations.
6. Use Postman to send HTTP requests and interpret API responses for testing and debugging.
7. Understand the stateless nature of REST APIs and the limitations of in-memory storage.
