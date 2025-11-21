from one.api import ONE
import argparse

def download_data():
    one = ONE(base_url='https://openalyx.internationalbrainlab.org', password='international', silent=True)
    eid = '4720c98a-a305-4fba-affb-bbfa00a724a4'
    # Download and load the left camera timestamps
    left_cam_times = one.load_dataset(eid, '_ibl_leftCamera.times.npy')
    print("Downloaded left camera timestamps.")

    # Download and load the spikes times for probe00
    spike_times = one.load_dataset(eid, 'spikes.times.npy', collection='alf/probe00/pykilosort', revision='2024-05-06')
    print("Downloaded spike times.")

def get_file_size():
    one = ONE(base_url='https://openalyx.internationalbrainlab.org', password='international', silent=True)
    eid = '4720c98a-a305-4fba-affb-bbfa00a724a4'
    
    total_size_in_mb = 0
    
    # Get size of left camera timestamps
    dset = one.alyx.rest('datasets', 'list', session=eid, name='_ibl_leftCamera.times.npy')[0]
    total_size_in_mb += dset['file_size'] / (1024 * 1024)
    
    # Get size of spike times
    dset = one.alyx.rest('datasets', 'list', session=eid, name='spikes.times.npy', collection='alf/probe00/pykilosort', revision='2024-05-06')[0]
    total_size_in_mb += dset['file_size'] / (1024 * 1024)
    
    print(f"{total_size_in_mb:.2f}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download or get file size of the IBL ONE dataset.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data()
