import os, requests

def download_data():
    url = "https://github.com/steevelaquitaine/projInference/raw/gh-pages/data/csv/data01_direction4priors.csv"
    fname = "data01_direction4priors.csv"
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
