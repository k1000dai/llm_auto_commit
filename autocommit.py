from urllib.request import Request, urlopen
import json
import subprocess

# git diff 取得
cp = subprocess.run(['git', 'diff','--staged'], encoding='utf-8', stdout=subprocess.PIPE)
diff = cp.stdout

url = "http://localhost:11434/api/generate"

prompt = f"""
<|user|>
Write a simple and understadable commit message for the following changes:

# Changes
{diff}

Plese output with format like below
<output>
<commit_message>"your commit message"</commit_message>
<misc>write some miscellaneous information</misc>
</output>

# Example
<output>
<commit_message>Fix bug</commit_message>
<misc>hoge</misc>
</output>

<|end|>
<|assistant|>
"""

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
response_text = response_json['response']

# git commit にコミットメッセージを渡す


try:
    commit_message = response_text.split('<commit_message>')[1].split('</commit_message>')[0]
    print(commit_message)
    y_n = input('Do you want to commit? [y/n]: ')
    if y_n == 'n':
        exit()
    subprocess.run(['git', 'commit', '-m', commit_message])
except Exception as e:
    print(response_text)