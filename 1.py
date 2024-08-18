import requests
import os
import json

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = response.json()

if not os.path.exists('json_files'):
    os.makedirs('json_files')


for i, item in enumerate(data):
    file_path = os.path.join('json_files', f'file_{i+1}.json')
    with open(file_path, 'w') as f:
        json.dump(item, f)

