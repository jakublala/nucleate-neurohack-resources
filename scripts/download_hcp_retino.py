import os
import requests
import tarfile
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
    DATA_DIR = "./hcp_retino"
    if not os.path.isdir(DATA_DIR):
      os.mkdir(DATA_DIR)

    fname = "hcp_retino.tgz"
    url = "https://osf.io/d25b4/download"

    if dry_run:
        get_file_size(url)
        return

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
          print(f"Download {fname} completed!")
          with tarfile.open(fname) as tfile:
            tfile.extractall(DATA_DIR)
    else:
        print("Data already downloaded.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download HCP retino data.')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run to get file size without downloading.')
    args = parser.parse_args()
    download_data(dry_run=args.dry_run)
