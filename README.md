# llm_auto_commit

This is a auto commit tool for git.
It uses local language model to generate commit message.

I came up with the idea when I see the article below.
https://zenn.dev/takaha4k/articles/7cd3ac44ee2c7b

## How to Install
### Step.1 install Ollama

 https://ollama.com/

### Step.2 install LLM
```
ollama run phi3
```
Now, this only supports phi3 model.
### Step.3 clone this repository and install
```
git clone https://github.com/k1000dai/llm_auto_commit.git
pip install .
```

## How to Use
if you have already staged files, you can use the command below.
```
gitac
```
and then, you can see the commit message generated by local language model.
example:
```
Implement installation instructions for llm-auto-commit package in README.md
    
Do you want to commit? [y/n]: y
```
if enter y , it will be committed.
