import requests

print(requests.__version__)

google = requests.get("http://google.com/teapot")

print(google)
