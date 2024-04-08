#!/usr/bin/python3
"""
Records all tasks for an employee based in employee_id.
Export the result in JSON format, named <user_id>.json
"""

import json
import sys
import urllib.request


def get_employee_todos(employee_id):
    """
    Records all tasks from all employees.
    """

    # Fetch employee details by id and employees todos
    employee_details_response = urllib.request.urlopen(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(employee_id))
    todos_response = urllib.request.urlopen(
        'https://jsonplaceholder.typicode.com/todos')

    # Convert response to JSON
    employee_details_data = json.loads(employee_details_response.read())
    todos_data = json.loads(todos_response.read())

    # Filter todos by employee's userId
    employee_todos_total = [todo for todo in todos_data
                            if todo.get('userId') ==
                            employee_details_data['id']]

    data = {
        employee_id: []
    }

    for todo in employee_todos_total:
        # Export employee's todos to JSON
        data[employee_id].append(
            {
                "username": employee_details_data['username'],
                "task": todo['title'],
                "completed": todo['completed']
            }
        )

    with open('{}.json'.format(employee_id), 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    employee_id = sys.argv[1]

    get_employee_todos(employee_id)
