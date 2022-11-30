#!/usr/bin/python3
"""Python script that uses a REST API to return info about an employee's Todo\
    list progress and exports the data in JSON format."""


def get_todos_json():
    import csv
    import json
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

    tasks_json = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user.get("username")
        tasks_json.append(task_dict)
    dict_json = {}
    dict_json[id] = tasks_json
    with open("{}.json".format(id), "w") as file:
        json.dump(dict_json, file)


if __name__ == '__main__':
    get_todos_json()
