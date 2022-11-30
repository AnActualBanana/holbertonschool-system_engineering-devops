#!/usr/bin/python3
"""Python script that uses a REST API to return info about an employee's Todo\
    list progress"""


def get_todos():
    import requests
    from sys import argv
    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()

    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()

    completed_tasks = []

    for task in todo:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed_tasks), len(todo)))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    get_todos()
