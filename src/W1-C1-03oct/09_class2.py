employees = [
    {
        "employee_id": 1,
        "name": "John",
        "salary": 50000,
    },
    {
        "employee_id": 2,
        "name": "Jane Smith",
        "salary": 50000,
    },
    {
        "employee_id": 3,
        "name": "Bob Johnson",
        "salary": 30000,
    },
    {
        "employee_id": 4,
        "name": "Alice Brown",
        "salary": 40000,
    },
    {
        "employee_id": 5,
        "name": "Charlie Wilson",
        "salary": 60000,
    }
]

for employee in employees:
    if len(employee["name"]) > 6 and employee["salary"] > 25000:
        print(f"{employee['name']} has a short name")