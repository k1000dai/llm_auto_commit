from urllib.request import Request, urlopen
import json

url = "http://localhost:11434/api/generate"

data = {
  "model": "phi3",
  "prompt": "write a short commit message within ten words",
  "stream": False,
}

headers = {'Content-Type': 'application/json'}

request = Request(url, data=json.dumps(data).encode(), headers=headers)
response = urlopen(request)

print(response.read().decode())
