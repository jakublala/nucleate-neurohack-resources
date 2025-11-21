import os
import requests
import zipfile
import argparse

def get_file_size(url):
    try:
        with requests.get(url, stream=True, allow_redirects=True) as response:
            response.raise_for_status()
            size = int(response.headers.get('content-length', 0))
            print(f"URL: {url}")
            print(f"File size: {size / 1024 / 1024:.2f} MB")
    except requests.exceptions.RequestException as e:
        print(f"!!! Failed to get file size: {e} !!!")

def download_data(dry_run=False):
    files_to_download = [
        {"url": "https://data.caltech.edu/records/s0vdx-0k302/files/task1_classic_classification.zip?download=1", "fname": "task1_classic_classification.zip"},
        {"url": "https://data.caltech.edu/records/s0vdx-0k302/files/calms21_convert_to_npy.py?download=1", "fname": "calms21_convert_to_npy.py"}
    ]

    if dry_run:
        for file_info in files_to_download:
            get_file_size(file_info["url"])
        return

    # Download data
    fname = files_to_download[0]['fname']
    url = files_to_download[0]['url']
    if not os.path.isfile(fname):
      try:
        r = requests.get(url)
      except requests.ConnectionError:
        print("!!! Failed to download data !!!")
      else:
        if r.status_code != requests.codes.ok:
          print("!!! Failed to download data !!!")
        else:
          print(f"Downloading {fname}...")
          with open(fname, "wb") as fid:
            fid.write(r.content)
          print("Download completed!")
    else:
      print('Data have already been downloaded!!!')

    if not os.path.exists('task1_classic_classification'):
      # Unzip the file
      with zipfile.ZipFile(fname, 'r') as zip_ref:
        zip_ref.extractall('.')


    # Download the script
    fname = files_to_download[1]['fname']
    url = files_to_download[1]['url']
    if not os.path.isfile(fname):
      try:
        r = requests.get(url)
      except requests.ConnectionError:
        print("!!! Failed to download data !!!")
      else:
        if r.status_code != requests.codes.ok:
          print("!!! Failed to download data !!!")
        else:
          print(f"Downloading {fname}...")
          with open(fname, "wb") as fid:
            fid.write(r.content)
          print("Download completed!")
    else:
        print("Script already downloaded.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download CalMS21 data.')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run to get file sizes without downloading.')
    args = parser.parse_args()
    download_data(dry_run=args.dry_run)
