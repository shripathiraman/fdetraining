from fastapi import FastAPI

app = FastAPI(title="FDE Week 1 API Employees")

# Sample data representing employees
employees = [
    {"id": 1, "name": "John Doe", "department": "Engineering"},
    {"id": 2, "name": "Jane Smith", "department": "Marketing"},
    {"id": 3, "name": "Bob Johnson", "department": "Sales"},
    {"id": 4, "name": "Alice Brown", "department": "HR"},
    {"id": 5, "name": "Charlie Davis", "department": "Finance"}
]

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}