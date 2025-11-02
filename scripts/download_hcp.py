import os, requests, tarfile

def download_data():
    fnames = ["hcp_rest.tgz",
              "hcp_task.tgz",
              "hcp_covariates.tgz",
              "atlas.npz"]
    urls = ["https://osf.io/bqp7m/download",
            "https://osf.io/s4h8j/download",
            "https://osf.io/x5p4g/download",
            "https://osf.io/j5kuc/download"]

    for fname, url in zip(fnames, urls):
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
            if fname.endswith(".tgz"):
                with tarfile.open(fname) as tfile:
                    tfile.extractall('./DATA')
      else:
          print(f"{fname} already downloaded.")

if __name__ == '__main__':
    download_data()
