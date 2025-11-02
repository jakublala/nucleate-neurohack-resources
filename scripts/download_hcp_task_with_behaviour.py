import os, requests, tarfile

def download_data():
    fname = "hcp_task.tgz"
    url = "https://osf.io/2y3fw/download"

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
            tfile.extractall('.')
    else:
        print("Data already downloaded.")

if __name__ == '__main__':
    download_data()
