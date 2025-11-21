import os
import subprocess
import sys
import argparse

def download_data():
    """
    Download OpenNeuro dataset ds006642 version 1.0.1.
    The derivatives folder contains all pre-processed data.
    """
    dataset_name = "ds006642"
    dataset_url = "https://openneuro.org/datasets/ds006642/versions/1.0.1"
    target_dir = "ds006642"
    
    # Check if datalad is installed
    try:
        import importlib.util
        spec = importlib.util.find_spec("datalad")
        if spec is None:
            raise ImportError("datalad not found")
    except (ImportError, AttributeError):
        print("datalad is not installed. Installing datalad...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "datalad"])
        print("datalad installed successfully.")
    
    # Check if dataset already exists
    if os.path.exists(target_dir):
        print(f"Dataset {dataset_name} already exists in {target_dir}.")
        print("Note: The 'derivatives' folder contains all pre-processed data.")
        return
    
    print(f"Downloading dataset {dataset_name} from OpenNeuro...")
    print(f"Dataset URL: {dataset_url}")
    print("Note: The 'derivatives' folder contains all pre-processed data.")
    print("This may take a while depending on the dataset size...")
    
    try:
        from datalad.api import install
        
        # Install the dataset
        dataset = install(
            source=dataset_url,
            path=target_dir
        )
        
        # Get all files in the dataset
        dataset.get(recursive=True)
        
        print(f"Dataset {dataset_name} downloaded successfully to {target_dir}.")
        print("Note: The 'derivatives' folder contains all pre-processed data.")
        
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        print("\nAlternative: You can manually download the dataset using:")
        print(f"  datalad install {dataset_url} {target_dir}")
        print(f"  cd {target_dir}")
        print("  datalad get .")
        raise

def get_file_size():
    print("N/A")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download or get file size of the ds006642 dataset.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data()
