import os, requests, zipfile, hashlib

def download_data(fname, url, expected_md5):
  if not os.path.isfile(fname):
    try:
      r = requests.get(url)
    except requests.ConnectionError:
      print("!!! Failed to download data !!!")
    else:
      if r.status_code != requests.codes.ok:
        print("!!! Failed to download data !!!")
      elif hashlib.md5(r.content).hexdigest() != expected_md5:
        print("!!! Data download appears corrupted !!!")
      else:
        with open(fname, "wb") as fid:
          fid.write(r.content)

def unzip_data(fname, path):
  if not os.path.exists(path):
    print("Unzipping data...", end='')
    zip_ref = zipfile.ZipFile(fname, 'r')
    zip_ref.extractall(path)
    zip_ref.close()
    print("Done.")

if __name__ == '__main__':
    fname_images = "kay_images.zip"
    url_images = "https://osf.io/ymvth/download"
    md5_images = "85626503513452455856a20316732163"
    download_data(fname_images, url_images, md5_images)
    path = "./kay_images"
    unzip_data(fname_images, path)
