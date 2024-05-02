from urllib.request import Request, urlopen
import json
import subprocess

# git diff 取得
cp = subprocess.run(['git', 'diff','--staged'], encoding='utf-8', stdout=subprocess.PIPE)
diff = cp.stdout#.replace('\n', ' ')

url = "http://localhost:11434/api/generate"

prompt = """
<|user|>
Generate a concise git commit message written in present tense for the following code diff with the given specifications below
Commit message must be a maximum of 10 characters.
Exclude anything unnecessary such as translation. Your entire response will be passed directly into git commit.

git diff --staged is as follows:
{}

<|end|>
<|assistant|>
""".format(diff)


data = {
  "model": "phi3",
  "prompt": prompt,
  "raw": True,
  "stream": False,
}

headers = {'Content-Type': 'application/json'}

request = Request(url, data=json.dumps(data).encode(), headers=headers)
response = urlopen(request)

response_json = json.loads(response.read().decode())

print("-----------------")
print(response_json['response'])
