import argparse
from allensdk.brain_observatory.behavior.behavior_project_cache import VisualBehaviorOphysProjectCache

def download_data():
    data_storage_directory = "./temp"
    cache = VisualBehaviorOphysProjectCache.from_s3_cache(cache_dir=data_storage_directory)
    print("AllenSDK cache setup complete.")

def get_file_size():
    print("N/A")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download or get file size of the Allen Visual Behavior dataset using the SDK.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data()
