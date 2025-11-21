import os
from one.api import ONE
from one.remote.aws import s3_download_file
import zipfile
import argparse
import requests

def download_data(event):
  assert event in ['firstMove', 'stimOn', 'feedback'], 'event must be one of "firstMove", "stimOn" or "feedback'

  # Dataset name
  fname = f'data_{event}.zip'
  # Remote location of data
  s3_data_path = f'sample_data/Neuromatch/{fname}'
  # Local location to download data to
  one = ONE(base_url='https://openalyx.internationalbrainlab.org', password='international', silent=True)
  save_path = one.cache_dir.joinpath('Neuromatch', fname)
  save_path.parent.mkdir(exist_ok=True, parents=True)

  # Download file
  file = s3_download_file(s3_data_path, save_path)
  # Unzip content
  with zipfile.ZipFile(file, 'r') as zip_ref:
    zip_ref.extractall(save_path.parent)
  print(f"Downloaded and unzipped {fname}.")

def get_file_size():
    events = ['firstMove', 'stimOn', 'feedback']
    total_size_in_mb = 0
    for event in events:
        url = f"https://ibl-brain-wide-map-public.s3.us-east-1.amazonaws.com/sample_data/Neuromatch/data_{event}.zip"
        try:
            with requests.get(url, stream=True, allow_redirects=True) as response:
                response.raise_for_status()
                size_in_bytes = int(response.headers.get('content-length', 0))
                size_in_mb = size_in_bytes / (1024 * 1024)
                total_size_in_mb += size_in_mb
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Warning: URL not found for event '{event}': {url}")
            else:
                raise e
    print(f"{total_size_in_mb:.2f}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download or get file size of the IBL BWM dataset.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data('stimOn')
