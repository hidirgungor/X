import json
import requests

result =  requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)

for i in result:
    if i["userId"] == 1:
        print(i["title"])
print(type(result))