from flask import Flask, request, jsonify
import emp

app = Flask(__name__)

@app.route("/")
def home():
    """Home route to check if the API is running."""
    return "<h1>Employee REST API in Python using Flask.</h1>"

@app.route("/emp", methods=['GET'])
def get_all_emp():
    """Retrieve all employees."""
    result = emp.get_all_emp()
    return jsonify(result), 200

@app.route("/emp/<int:emp_id>", methods=['GET'])
def get_emp_by_id(emp_id):
    """Retrieve an employee by their ID."""
    result = emp.get_emp_by_id(emp_id)
    if result is None:
        return jsonify({"message": "Employee not found"}), 404
    else:
        return jsonify(result), 200

@app.route("/emp", methods=["POST"])
def create_emp():
    """Create a new employee."""
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    emp_id = emp.create_emp(data)
    return jsonify({"message": "Employee created", "emp_id": emp_id}), 201

@app.route("/emp/<int:emp_id>", methods=['PUT'])
def update_emp(emp_id):
    """Update an existing employee's details."""
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    department = data.get("department", "")
    age = data.get("age", 0)
    
    urow = emp.update_emp(first_name, last_name, age, department, emp_id)
    if urow == 0:
        return jsonify({"message": "Invalid employee id"}), 404
    else:
        return jsonify({"message": "Employee updated"}), 200

@app.route("/emp/<int:emp_id>", methods=['DELETE'])
def delete_emp(emp_id):
    """Delete an employee."""
    drow = emp.delete_emp(emp_id)
    if drow == 0:
        return jsonify({"message": "Invalid employee id"}), 404
    else:
        return jsonify({"message": "Employee deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)