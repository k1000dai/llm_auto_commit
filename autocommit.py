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
{}
'''

Follow the format below.

<prefix>your prefix here</prefix> 
<commit>your commit message here</commit>

prefix list:
- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- refactor: A code change that neither fixes a bug nor adds a feature
- perf: A code change that improves performance
- test: Adding missing or correcting existing tests
- build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- ci: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- chore: Other changes that don't modify src or test files
- revert: Reverts a previous commit
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
print("--------")
print(response_json['response'])
print("--------")