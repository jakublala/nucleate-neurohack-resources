from allensdk.brain_observatory.behavior.behavior_project_cache import VisualBehaviorOphysProjectCache

def download_data():
    data_storage_directory = "./temp"
    cache = VisualBehaviorOphysProjectCache.from_s3_cache(cache_dir=data_storage_directory)
    print("AllenSDK cache setup complete.")

if __name__ == '__main__':
    download_data()
