import requests

url = "http://127.0.0.1:8000/stu_info/2"

r = requests.get(url =url)

data = r.json()
print(data)