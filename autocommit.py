from urllib.request import Request, urlopen
import json
import subprocess

# git diff 取得
cp = subprocess.run(['git', 'diff','--staged'], encoding='utf-8', stdout=subprocess.PIPE)
diff = cp.stdout#.replace('\n', ' ')
print(diff)

url = "http://localhost:11434/api/generate"

prompt = """
<|system|>
Only Write the commit message. Do not output without commit message for saving tokens.<|end|>
<|user|>
Write the simple and understandable commit message by reading git diff below.
----
diff --git a/test b/test
index 49fe595..e6e041e 100644
--- a/test
+++ b/test
@@ -1 +1,2 @@
-# llm_auto_commit
\ No newline at end of file
+# llm_auto_commit
+This is a simple script that automatically commits and pushes changes to a git repository. It is intended to be used in a cron job to automatically commit changes to a repository at a set interval.
\ No newline at end of file
<|end|>
<|assistant|>
commit message: "test is updated"<|end|>
<|end|>
<|user|>
Write the simple and understandable commit message by reading git diff below.
----
diff --git a/hoge b/hoge
index 49fe595..e6e041e 100644
--- a/test
+++ b/test
@@ -1 +1,2 @@
\ No newline at end of file
+ hoeghoge
<|end|>
<|assistant|>
commit message: "write discription about hoge"<|end|>
<|end|>
<|user|>
Write the simple and understandable commit message by reading git diff below.
----
{}
<|end|>
<|assistant|>
commit message: 
""".format(diff)

print(prompt)

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