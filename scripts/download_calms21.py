import os, requests, zipfile

def download_data():
    fname = 'task1_classic_classification.zip'
    url = "https://data.caltech.edu/records/s0vdx-0k302/files/task1_classic_classification.zip?download=1"

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
    fname = 'calms21_convert_to_npy.py'
    url = "https://data.caltech.edu/records/s0vdx-0k302/files/calms21_convert_to_npy.py?download=1"

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
    download_data()
