import os
import requests
import json
from pathlib import Path
import argparse

def download_data(dry_run=False):
    # set path for data
    root = r'./data/Zhong_et_al_2025'
    Path(root).mkdir(parents=True, exist_ok=True)

    # files required for this project
    file_ID = [54866153, 54866354, 54184211, 54866333, 54184214, 54866237, 54184028, 54866150, 54184031, 54183863, 54183860, 54183914, 54183917]

    BASE_URL = 'https://api.figshare.com/v2'
    r = requests.get(BASE_URL + '/articles/' + str(28811129))
    file_metadata = json.loads(r.text)

    if dry_run:
        total_size = 0
        for file in file_metadata['files']:
            if file['id'] in file_ID:
                total_size += file['size']
                print(f"File: {file['name']}, Size: {file['size'] / 1024 / 1024:.2f} MB")
        print(f"Total download size: {total_size / 1024 / 1024:.2f} MB")
        return

    for file in file_metadata['files']:
      if file['id'] in file_ID:
        fn = os.path.join(root, file['name'])
        if not os.path.isfile(fn):
          print(f"Downloading {file['name']}...")
          response = requests.get(BASE_URL + '/file/download/' + str(file['id']))
          open(fn, 'wb').write(response.content)
    print("Download complete.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download visual learning 80k neurons data.')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run to get file size without downloading.')
    args = parser.parse_args()
    download_data(dry_run=args.dry_run)
