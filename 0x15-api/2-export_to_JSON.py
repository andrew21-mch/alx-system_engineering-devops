#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(userId))
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        taskList.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.json().get('username')
            })

    records = {
        "{}".format(userId): taskList
    }

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(records, f)
