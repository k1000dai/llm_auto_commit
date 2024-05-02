from urllib.request import Request, urlopen
import json
import subprocess

# git diff 取得
cp = subprocess.run(['git', 'diff','--staged'], encoding='utf-8', stdout=subprocess.PIPE)
diff = cp.stdout#.replace('\n', ' ')

url = "http://localhost:11434/api/generate"

prompt = """
<|user|>
Write the simple and understandable commit message about 10 words by reading git diff below.

git diff --staged is as follows.
'''
[git diff --staged is here]
'''

The commit message should be written as follows.
Only provide the commit message, do not include the explanation of the commit message.

[COMMIT]your commit message here

<|end|>
<|assistant|>
[COMMIT]commit message
<|end|>
<|user|>
Write the simple and understandable commit message about 10 words by reading git diff below.

git diff --staged is as follows.
'''
[git diff --staged is here]
'''

The commit message should be written as follows.
Only provide the commit message, do not include the explanation of the commit message.

[COMMIT]your commit message here

<|end|>
<|assistant|>
[COMMIT]commit message
<|end|>
<|user|>
Write the simple and understandable commit message about 10 words by reading git diff below.

git diff --staged is as follows.
'''
{}
'''

The commit message should be written as follows.
Only provide the commit message, do not include the explanation of the commit message.

[COMMIT]your commit message here

<|end|>
<|assistant|>
[COMMIT]
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

print(response_json['response'])
