import os, requests

def download_data():
    fname = 'joystick_track.npz'
    url = "https://osf.io/6jncm/download"

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
        print("Data already downloaded.")

if __name__ == '__main__':
    download_data()
