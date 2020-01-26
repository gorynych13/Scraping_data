import requests
import json
from pprint import pprint
main_link = 'https://api.github.com/users/gorynych13/repos'
response = requests.get(main_link)
data = json.loads(response.text)
output = []

for i in data:
    name = i['name']
    html_url = i['html_url']
    url = i['url']
    output.append({'name': name, 'html_url': html_url, 'url': url})

pprint(output)

with open("repos.json", "w") as write_file:
    json.dump(output, write_file)
