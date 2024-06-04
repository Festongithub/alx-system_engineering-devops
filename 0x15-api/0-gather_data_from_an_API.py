#!/usr/bin/python3

"""
Script that for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys
import json


url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    userId = sys.argv[1]

    users_uri = '{}/users?id={}'.format(url, userId)

    response = requests.get(users_uri)
    data = response.text
    # load the data
    data = json.loads(data)
    # extract name
    name = data[0].get('name')

    # Task for the employees
    task_url = '{}/todos?userId={}'.format(url, userId)

    response = requests.get(task_url)
    tasks = response.text
    tasks = json.loads(tasks)

    # initialize list
    completed = 0
    total_tasks = len(tasks)

    comp_task = []

    for task in tasks:
        if task.get('completed'):
            comp_task.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))

    for task in comp_task:
        print("\t {}".format(task.get('title')))
