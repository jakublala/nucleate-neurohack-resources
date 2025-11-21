import os, requests, argparse

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

def get_file_size():
    url = "https://ndownloader.figshare.com/files/28470255"
    with requests.get(url, stream=True, allow_redirects=True) as response:
        response.raise_for_status()
        size_in_bytes = int(response.headers.get('content-length', 0))
        size_in_mb = size_in_bytes / (1024 * 1024)
        print(f"{size_in_mb:.2f}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download or get file size of the Allen Visual Behavior dataset.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data()
