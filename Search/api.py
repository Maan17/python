import requests
from time import sleep

try:
    response = requests.get("https://wordsapiv1.p.mashape.com/words/example/definitions")
    print(response.status_code)
except requests.exceptions.ConnectionError as e:
    print("No response")
