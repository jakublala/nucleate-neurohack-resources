import os, requests

def download_data():
    fname = "allen_visual_behavior_2p_change_detection_familiar_novel_image_sets.parquet"
    url = "https://ndownloader.figshare.com/files/28470255"

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
