import os, requests, zipfile, subprocess, argparse

def get_file_size(url):
    try:
        with requests.get(url, stream=True, allow_redirects=True) as response:
            response.raise_for_status()
            size = int(response.headers.get('content-length', 0))
            print(f"URL: {url}")
            print(f"File size: {size / 1024 / 1024:.2f} MB")
    except requests.exceptions.RequestException as e:
        print(f"!!! Failed to get file size: {e} !!!")

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

def download_data(dry_run=False):
    fnames = ['rdms.zip', 'affordances.zip']
    urls = ['https://osf.io/dsnq6/download', 'https://osf.io/zcgub/download']
    dests = ['rdms/', 'affordances/']

    if dry_run:
        for url in urls:
            get_file_size(url)
        return

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
    parser = argparse.ArgumentParser(description='Download Bonner navigational affordances data.')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run to get file size without downloading.')
    args = parser.parse_args()
    download_data(dry_run=args.dry_run)
