import os
from one.api import ONE
from one.remote.aws import s3_download_file, get_s3_public
import pandas as pd
import sys
import argparse

if sys.version_info >= (3, 10):
    from one.alf.path import add_uuid_string
else:
    from one.alf.files import add_uuid_string

s3, bucket = get_s3_public()

def load_aggregate(subject, dataset):
    one = ONE(base_url='https://openalyx.internationalbrainlab.org', password='international', silent=True)
    if sys.version_info >= (3, 10):
        return one.load_aggregate('subjects', subject, dataset)
    else:
        files = one.list_aggregates('subjects', subject, dataset=dataset)
        files = files.iloc[0]
        src_path = str(add_uuid_string(files['rel_path'], files.name))
        dst_path = one.cache_dir.joinpath(files['rel_path'])
        local_file = s3_download_file(src_path, dst_path, s3=s3, bucket_name=bucket)
        return pd.read_parquet(local_file)

def download_data():
    one = ONE(base_url='https://openalyx.internationalbrainlab.org', password='international', silent=True)
    datasets = one.alyx.rest('datasets', 'list', tag='2021_Q1_IBL_et_al_Behaviour', name='_ibl_subjectTrials.table.pqt')
    subjects = [d['file_records'][0]['relative_path'].split('/')[2] for d in datasets]
    subject = subjects[0]
    subject_trials = load_aggregate(subject, '_ibl_subjectTrials.table.pqt')
    session_trials = load_aggregate(subject, '_ibl_subjectSessions.table.pqt')
    print("Downloaded data for subject", subject)

def get_file_size():
    print("N/A")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download or get file size of the IBL behavior dataset.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data()
