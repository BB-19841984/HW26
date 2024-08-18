import aiohttp
import asyncio
import os
import json

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
            data = await response.json()
            return data

async def save_files(data):
    
    if not os.path.exists('json_files'):
        os.makedirs('json_files')

    
    for i, item in enumerate(data):
        file_path = os.path.join('json_files', f'file_{i+1}.json')
        with open(file_path, 'w') as f:
            json.dump(item, f)

async def main():
    data = await fetch_data()
    await save_files(data)

asyncio.run(main())
