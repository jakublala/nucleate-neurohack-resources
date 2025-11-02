import os
import requests
import json
from pathlib import Path

def download_data():
    # set path for data
    root = r'./data/Zhong_et_al_2025'
    Path(root).mkdir(parents=True, exist_ok=True)

    # files required for this project
    file_ID = [54866153, 54866354, 54184211, 54866333, 54184214, 54866237, 54184028, 54866150, 54184031, 54183863, 54183860, 54183914, 54183917]

    BASE_URL = 'https://api.figshare.com/v2'
    r = requests.get(BASE_URL + '/articles/' + str(28811129))
    file_metadata = json.loads(r.text)
    for file in file_metadata['files']:
      if file['id'] in file_ID:
        fn = os.path.join(root, file['name'])
        if not os.path.isfile(fn):
          print(f"Downloading {file['name']}...")
          response = requests.get(BASE_URL + '/file/download/' + str(file['id']))
          open(fn, 'wb').write(response.content)
    print("Download complete.")

if __name__ == '__main__':
    download_data()
