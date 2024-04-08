#!/usr/bin/python3
"""
For a given employee ID, returns information
about his/her TODO list progress.
Export the result in JSON format, named <user_id>.json
"""

import csv
import json
import sys
import urllib.request


def get_all_employees_todos():
    """
    Retrieve all 10 employees' todos, exports information
    about his/her TODO list progess in JSON format
    """

    data = {}

    for employee_id in range(1,10):
        # Fetch employee details by id and employees todos
        employee_details_response = urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
        todos_response = urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/todos')
        
        # Convert response to JSON
        employee_details_data = json.loads(employee_details_response.read())
        todos_data = json.loads(todos_response.read())

        # Filter todos by employee's userId
        employee_todos_total = [todo for todo in todos_data
                                if todo.get('userId') ==
                                employee_details_data['id']]

        data.update({
            employee_id: []
        })

        for todo in employee_todos_total:
            # Export employee's todos to JSON
            data[employee_id].append(
                {
                    "username": employee_details_data['username'],
                    "task": todo['title'],
                    "completed": todo['completed']
                }
            )

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    get_all_employees_todos()
