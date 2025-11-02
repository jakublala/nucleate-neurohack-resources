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

if __name__ == '__main__':
    download_data()
