import os, requests, tarfile

def download_data():
    DATA_DIR = "./hcp_retino"
    if not os.path.isdir(DATA_DIR):
      os.mkdir(DATA_DIR)

    fname = "hcp_retino.tgz"
    url = "https://osf.io/d25b4/download"

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
    download_data()
