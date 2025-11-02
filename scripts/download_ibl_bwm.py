import os
from one.api import ONE
from one.remote.aws import s3_download_file
import zipfile

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

if __name__ == '__main__':
    download_data('stimOn')
