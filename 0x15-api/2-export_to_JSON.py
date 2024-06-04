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
    user_name = data[0].get('username')

    # Task for the employees
    task_url = '{}/todos?userId={}'.format(url, userId)

    response = requests.get(task_url)
    tasks = response.text
    tasks = json.loads(tasks)

    user_dict = str(userId)

    # csv file build

    csv_file = {user_dict: []}

    for task in tasks:
        json_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
                }
        csv_file[user_dict].append(json_data)
    json_encoded_data = json.dumps(csv_file)
    with open('{}.json'.format(userId), 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
