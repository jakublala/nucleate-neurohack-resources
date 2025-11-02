import os, requests, zipfile, subprocess

def Unzip(fname, destinationDirectory):
  try:
    with zipfile.ZipFile(fname, 'r') as zipObj:
      zipObj.extractall(destinationDirectory)
  except:
    print("An exception occurred extracting with Python ZipFile library.")
    print("Attempting to extract using 7zip")
    subprocess.Popen(["7z", "e",
                      f"{fname}",
                      f"-o{destinationDirectory}",
                      "-y"])

def download_data():
    fnames = ['rdms.zip', 'affordances.zip']
    urls = ['https://osf.io/dsnq6/download', 'https://osf.io/zcgub/download']
    dests = ['rdms/', 'affordances/']
    for fname, url, dest in zip(fnames, urls, dests):
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
            with open(fname, "wb") as fd:
              fd.write(r.content)
            Unzip(fname, dest)
            print(f'Download/Extraction of {fname} has been completed!')
      else:
        print(f"{fname} already downloaded.")

if __name__ == '__main__':
    download_data()
