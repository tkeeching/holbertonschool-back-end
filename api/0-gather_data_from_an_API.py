#!/usr/bin/python3

import urllib.request
import sys
import json

# Fetch employee details by id and employees todos
employee_id = sys.argv[1]
employee_details_response = urllib.request.urlopen(
    'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
todos_response = urllib.request.urlopen(
    'https://jsonplaceholder.typicode.com/todos')

# Convert response to JSON
employee_details_data = json.loads(employee_details_response.read())
todos_data = json.loads(todos_response.read())

# Filter todos by employee's userId
employee_todos_total = [todo for todo in todos_data
                        if todo.get('userId') == employee_details_data['id']]
employee_todos_completed = [todo for todo in employee_todos_total
                            if todo.get('completed') is True]

# Display result
print('Employee {} is done with tasks({}/{}):'
      .format(employee_details_data['name'],
              len(employee_todos_completed),
              len(employee_todos_total)))

for todo in employee_todos_completed:
    print('\t{}'.format(todo['title']))
