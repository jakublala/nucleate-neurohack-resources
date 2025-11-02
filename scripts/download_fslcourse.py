import os, shutil, requests, tarfile

def download_data():
    DATA_DIR = "./fslcourse"
    if not os.path.isdir(DATA_DIR):
      os.mkdir(DATA_DIR)

    fname = "fslcourse.tgz"
    url = "https://osf.io/syt65/download/"

    if not os.path.isfile(fname):
      try:
        r = requests.get(url)
      except requests.ConnectionError:
        print("!!! Failed to download data !!!")
      else:
        if r.status_code != requests.codes.ok:
          print("!!! Failed to download data !!!")
        else:
          print("Downloading data...")
          with open(fname, "wb") as fid:
            fid.write(r.content)
          # open file
          with tarfile.open(fname) as fzip:
            fzip.extractall(DATA_DIR)
          print("Download completed!")
    else:
      print("Data have been already downloaded!")

if __name__ == '__main__':
    download_data()
