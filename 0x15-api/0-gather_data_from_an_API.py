#!/usr/bin/python3

"""This module works with API"""

import requests
import sys


def get_employee_name(employee_id):
    """Gets the employee name"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data['name']
    else:
        print(f"Failed to fetch user data: {response.status_code}")
        return None


def get_todo_list_progress(employee_id):
    """Gets the list for the employee"""
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todo_url)

    if response.status_code == 200:
        todos = response.json()

        # Filter the tasks based on the given employee ID
        employee_todos = [todo for todo in todos if todo['userId']
                          == employee_id]

        if employee_todos:
            employee_name = get_employee_name(employee_id)
            if not employee_name:
                return

            total_tasks = len(employee_todos)
            completed_tasks = [todo for todo in employee_todos
                               if todo['completed']]
            num_completed_tasks = len(completed_tasks)

            print(f"Employee {employee_name} is done with tasks\
                  ({num_completed_tasks}/{total_tasks}): ")

            for todo in completed_tasks:
                print(f"\t {todo['title']}")
        else:
            print(f"No TODOs found for employee ID {employee_id}")
    else:
        print(f"Failed to fetch data: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_todo_list_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
