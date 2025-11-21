import argparse
import requests
from pynwb import NWBHDF5IO
from dandi.dandiapi import DandiAPIClient
import fsspec
import h5py

def download_data():
    sbj, session = 1, 3
    with DandiAPIClient() as client:
        asset = client.get_dandiset("000055").get_asset_by_path(
            "sub-{0:>02d}/sub-{0:>02d}_ses-{1:.0f}_behavior+ecephys.nwb".format(sbj, session)
        )
        s3_path = asset.get_content_url(follow_redirects=1, strip_query=True)

    fs = fsspec.filesystem("http")
    with fs.open(s3_path, "rb") as f:
        with h5py.File(f, "r") as file:
            with NWBHDF5IO(file=file, mode='r', load_namespaces=True) as io:
                nwbfile = io.read()
                print("Successfully streamed data from DANDI.")

def get_file_size():
    with DandiAPIClient() as client:
        asset = client.get_dandiset("000055").get_asset_by_path(
            "sub-01/sub-01_ses-3_behavior+ecephys.nwb"
        )
        s3_path = asset.get_content_url(follow_redirects=1, strip_query=True)
    
    response = requests.head(s3_path)
    size_in_bytes = int(response.headers.get('content-length', 0))
    size_in_mb = size_in_bytes / (1024 * 1024)
    print(f"{size_in_mb:.2f}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download or get file size of the AJILE12 dataset.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data()
