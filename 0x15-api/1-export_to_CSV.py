#!/usr/bin/python3

"""
Script that for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
import sys


url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    userId = sys.argv[1]

    users_uri = '{}/users?id={}'.format(url, userId)

    response = requests.get(users_uri)
    data = response.text
    # load the data
    data = json.loads(data)
    # extract name
    name = data[0].get('username')

    # Task for the employees
    task_url = '{}/todos?userId={}'.format(url, userId)

    response = requests.get(task_url)
    tasks = response.text
    tasks = json.loads(tasks)

    # build the csv data docs

    docs = ""
    for task in tasks:
        docs += '"{}", "{}", "{}", "{}"\n'.format(
                userId,
                name,
                task['completed'],
                task['title']
                )
    with open('{}.csv'.format(userId), 'w', encoding='UTF8') as user_file:
        user_file.write(docs)
