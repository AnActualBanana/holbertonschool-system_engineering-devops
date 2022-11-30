#!/usr/bin/python3
"""Python script that uses a REST API to return info about an employee's Todo\
    list progress and exports it in CSV format."""


def get_todos_csv():
    import csv
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

    with open("{}.csv".format(id), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([int(id), user.get("username"),
                            task.get("completed"), task.get("title")])


if __name__ == '__main__':
    get_todos_csv()
