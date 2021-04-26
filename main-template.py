import json
import requests
from bs4 import BeautifulSoup

# crawler url
urls = ["http://140.xxx.xxx.xxx/", "http://140.xxx.xxx.xxx/"]
# name for showing in slack
printers = ["HP Color LaserJet M154nw", "HP LaserJet 400 M401dne"]
# slack hoop api
s_url = 'https://hooks.slack.com/services/xxx'

messages = ""
ink_info = []

for url, printer in zip(urls, printers):
    messages = messages + "\n"+ printer + "\n"

    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')

    for i in soup.find_all('td',  {"class": "width25"}):
        _temp = i.tr.get_text()
        _temp = _temp.strip()
        _temp = _temp.replace("\u202c", "")
        _temp = _temp.replace("\u202d", "")
        _temp = "&".join(_temp.split())
        
        if len(_temp.split("&")) == 6:
            color, _, hp_ink, ink_color_number, percent, _ = _temp.split("&")
            # print(color, hp_ink, ink_color_number, percent)
        else:
            color, _, _, hp_ink, ink_color_number, percent, _ = _temp.split("&")
            # print(color, hp_ink, ink_color_number, percent)
        messages = messages + "{} {} {} {}\n".format(color, hp_ink, ink_color_number, percent)
    
# print(messages)

# HTTP POST Request

dict_headers = {'Content-type': 'application/json'}

dict_payload = {
    "text": messages}
json_payload = json.dumps(dict_payload)

rtn = requests.post(s_url, data=json_payload, headers=dict_headers)
print(rtn.text)