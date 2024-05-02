from urllib.request import Request, urlopen
import json
import subprocess

# git diff 取得
cp = subprocess.run(['git', 'diff','--staged'], encoding='utf-8', stdout=subprocess.PIPE)
diff = cp.stdout#.replace('\n', ' ')
print(diff)

url = "http://localhost:11434/api/generate"

data = {
  "model": "phi3",
  "prompt": "Only output the commit message for fast output. write a good commit message about 5 words for below code : {} ".format(diff),
  "stream": False,
}

headers = {'Content-Type': 'application/json'}

request = Request(url, data=json.dumps(data).encode(), headers=headers)
response = urlopen(request)

response_json = json.loads(response.read().decode())
print("--------")
print(response_json['response'])
print("--------")