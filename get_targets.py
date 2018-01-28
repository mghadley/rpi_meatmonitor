import time
import requests
import json

payload = {'token' : 'jua6BxY39LvmHXQNzHFzusKR'}
url = 'https://meatmonitor.herokuapp.com/api/v1/chambers/1'

while True:
    response = requests.get(url, params=payload)
    chamber = json.loads(response.text)
    data = {
        'target_temp' : float(chamber['target_temp']),
        'target_humidity' : float(chamber['target_humidity'])
    }
    with open('targets.txt', 'w') as outfile: json.dump(data, outfile)
    time.sleep(1)
