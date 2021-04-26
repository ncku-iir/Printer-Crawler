# Printer-Crawler
## Introduction
A printer ink usage notification tool.

## Installation and Usage
### Prerequisite
This tool is build on slack webhook and python crawler
1. https://api.slack.com/messaging/webhooks
2. python Beautiful Soup package

### Usage
We use windows10 for demo.
1. Copy *-template file
```
cp exec-template.bat exec.bat
cp main-template.py main.py
```
2. Editting `exec.bat` and `main.py` and replacing {} with your local environment
`call conda activate {}` -> `call conda activate myenv`
3. setting task scheduler