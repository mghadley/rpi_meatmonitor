import time
import json
import requests

token = 'jua6BxY39LvmHXQNzHFzusKR'
url = 'https://meatmonitor.herokuapp.com/api/v1/chambers/1'

while True:
    with open('state.txt', 'r') as file: payload = json.load(file)
    payload['token'] = token
    response = requests.put(url, json=payload)
    time.sleep(5)
