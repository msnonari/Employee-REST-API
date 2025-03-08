# Employee CRUD API

A simple Employee CRUD (Create, Read, Update, Delete) REST API built using Python and Flask, with SQLite as the database. This API allows you to manage employee records, including creating new employees, retrieving employee details, updating existing employee information, and deleting employees.

## Features

- Retrieve all employees
- Retrieve an employee by their ID
- Create a new employee
- Update an existing employee's details
- Delete an employee

## Requirements

- Python 3.6+
- Flask
- SQLite

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/msnonari/Employee-REST-API.git
   cd Employee-REST-API
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Create the SQLite database and the `Employee` table:

   ```sh
   sqlite3 EmpData.db < schema.sql
   ```

## Usage

1. Run the Flask application:

   ```sh
   python app.py
   ```

2. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

- `GET /`: Home route to check if the API is running.
- `GET /emp`: Retrieve all employees.
- `GET /emp/<int:emp_id>`: Retrieve an employee by their ID.
- `POST /emp`: Create a new employee.
- `PUT /emp/<int:emp_id>`: Update an existing employee's details.
- `DELETE /emp/<int:emp_id>`: Delete an employee.

## Example Requests

### Retrieve all employees

```sh
curl -X GET http://127.0.0.1:5000/emp
```

### Retrieve an employee by ID

```sh
curl -X GET http://127.0.0.1:5000/emp/1
```

### Create a new employee

```sh
curl -X POST http://127.0.0.1:5000/emp -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "age": 30, "email": "john.doe@example.com", "gender": "Male", "job_title": "Developer", "department": "IT", "salary": 60000, "hire_date": "2023-10-01"}'
```

### Update an existing employee

```sh
curl -X PUT http://127.0.0.1:5000/emp/1 -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "age": 31, "department": "HR"}'
```

### Delete an employee

```sh
curl -X DELETE http://127.0.0.1:5000/emp/1
```

## License

This project is licensed under the MIT License.
