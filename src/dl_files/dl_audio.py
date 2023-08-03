import requests
import os
import re
import json
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()
TITLE_URL_JSON = os.getenv('TITLE_URL_JSON')
AUDIO_PATH_INIT = os.getenv("AUDIO_PATH_INIT")
PROC_TITLES = os.getenv("PROC_TITLES")
'''
def dl_audio():

    with open(TITLE_URL_JSON, 'r') as f:
        data = json.load(f)

    processed_titles = set()

    for title, url in tqdm(data.items()):
        if title not in processed_titles:
            response = requests.get(url)
            content = response.content
            file_name = re.sub('[<>:"/\\|?*]', '_', title) + ".mp3"
            with open(os.path.join(AUDIO_PATH_INIT, file_name), 'wb') as f:
                f.write(content)
                processed_titles.add(title)

    with open(PROC_TITLES, 'w') as f:
        for title in processed_titles:
            f.write(title + '\n')
'''
with open(TITLE_URL_JSON, "r") as f1:
    data = json.load(f1)

with open(PROC_TITLES, "r") as f2:
    titles = set(f2.read().splitlines())

for title, url in tqdm(data.items()):
    if title not in titles:
        response = requests.get(url)
        filename = os.path.join("Test" + ".mp3")
        with open(filename, "wb") as f:
            f.write(response.content)
        titles.add(title)

with open(PROC_TITLES, "w") as f2:
    for title in titles:
        f2.write(title + "\n")
