#!/usr/bin/python3
"""
For a given employee ID, returns information
about his/her TODO list progress.
Export the result to a CS V file, named <user_id>.csv
"""

import csv
import json
import sys
import urllib.request


def get_todos_by_id(employee_id):
    """
    For a given employee ID, returns information
    about his/her TODO list progess
    """

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
    employee_todos_completed = [todo for todo in employee_todos_total
                                if todo.get('completed') is True]

    # Export to CSV
    with open('{}.csv'.format(employee_id), 'w') as csvfile:
        writer = csv.writer(csvfile)
        for todo in employee_todos_total:
            todo_completed_status = 'True' if todo['completed'] else 'False'
            writer.writerow(
                [employee_id,
                 employee_details_data['username'],
                 todo_completed_status,
                 todo['title']])


if __name__ == "__main__":
    employee_id = sys.argv[1]

    get_todos_by_id(employee_id)
