import requests

test = requests.get('https://www.google.com')
print(test.text)