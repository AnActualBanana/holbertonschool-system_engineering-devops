#!/usr/bin/python3
"""Python script that uses a REST API to return info about all employees' Todo\
    list progress"""


def get_all_todos():
    import csv
    import json
    import requests
    from sys import argv
    user = requests.get("https://jsonplaceholder.typicode.com/users").json()

    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    completed_tasks = []

    with open("all_employees_todo.json", 'w') as file:
        todo_dict = {employee.get('id'): [{
                'task': task.get('title'),
                'username': employee.get('username'),
                'completed': task.get('completed')
            } for task in todo if employee.get('id') == task.get('userId')
            ] for employee in user}
        json.dump(todo_dict, file)


if __name__ == '__main__':
    get_all_todos()
