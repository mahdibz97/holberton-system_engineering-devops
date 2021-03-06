#!/usr/bin/python3
""" extend Python script to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(argv[1])
    employee_name = requests.get("{}/users/{}".format(url, user_id)).json()
    task_num = requests.get("{}/todos?userId={}".format(url, user_id)).json()
    tasks = []
    json_file = {}
    dic = {}
    for task in task_num:
        json_file['task'] = task.get('title')
        json_file['completed'] = task.get('completed')
        json_file['username'] = employee_name.get('username')
        tasks.append(json_file)
        json_file = {}
    dic[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(dic, jsonfile)
