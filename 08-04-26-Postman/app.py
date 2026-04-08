import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Data
employees = [
    {'id': 1, 'name': 'Ashley'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Joe'}
]

nextEmployeeId = 4

# Helper Functions
def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)

def employee_is_valid(employee):
    if "name" not in employee:
        return False
    return True

# GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees), 200

# GET single employee
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    employee = get_employee(id)
    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404
    return jsonify(employee), 200

# POST (Create employee)
@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = request.get_json()

    if not employee or not employee_is_valid(employee):
        return jsonify({'error': 'Invalid employee properties'}), 400

    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)

    return jsonify(employee), 201

# PUT (Update employee)
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = get_employee(id)

    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404

    updated_data = request.get_json()

    if not updated_data or not employee_is_valid(updated_data):
        return jsonify({'error': 'Invalid employee properties'}), 400

    employee.update(updated_data)
    return jsonify(employee), 200

# DELETE employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employee = get_employee(id)

    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404

    employees = [e for e in employees if e['id'] != id]
    return jsonify({'message': 'Deleted successfully'}), 200

# Run server
if __name__ == '__main__':
    app.run(debug=True, port=5000)