import time
import json
import requests
import logging
logging.basicConfig(filename='meatmonitor.log',level=logging.ERROR)

token = 'jua6BxY39LvmHXQNzHFzusKR'
url = 'https://meatmonitor.herokuapp.com/api/v1/chambers/1'

try:
    while True:
        with open('state.txt', 'r') as file: payload = json.load(file)
        payload['token'] = token
        response = requests.put(url, json=payload)
        time.sleep(5)
except Exception as e: logging.exception(e)
