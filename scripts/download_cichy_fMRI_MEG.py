import os, zipfile, requests

def download_data():
    fname = 'data.zip'
    url = "https://osf.io/7vpyh/download"

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
          with zipfile.ZipFile(fname, 'r') as zip_ref:
            zip_ref.extractall('data/')
          print("Download completed!")
    else:
        print("Data already downloaded.")

if __name__ == '__main__':
    download_data()
