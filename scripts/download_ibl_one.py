from one.api import ONE

def download_data():
    one = ONE(base_url='https://openalyx.internationalbrainlab.org', password='international', silent=True)
    eid = '4720c98a-a305-4fba-affb-bbfa00a724a4'
    # Download and load the left camera timestamps
    left_cam_times = one.load_dataset(eid, '_ibl_leftCamera.times.npy')
    print("Downloaded left camera timestamps.")

    # Download and load the spikes times for probe00
    spike_times = one.load_dataset(eid, 'spikes.times.npy', collection='alf/probe00/pykilosort', revision='2024-05-06')
    print("Downloaded spike times.")

if __name__ == '__main__':
    download_data()
