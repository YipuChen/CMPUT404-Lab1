import requests

print(requests.__version__)

google = requests.get("http://google.com/teapot")

print(google)

var = requests.get("https://raw.githubusercontent.com/YipuChen/CMPUT404-Lab1/master/Lab1.py")

print(var.content)
