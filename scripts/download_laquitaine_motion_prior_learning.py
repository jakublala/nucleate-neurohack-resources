import argparse

def download_data():
    print("This notebook does not download any external data. All data is generated synthetically within the notebook using `numpy` and `scipy`.")

def get_file_size():
    print("0.00")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get file size of the Laquitaine motion prior learning dataset.")
    parser.add_argument('--dry-run', action='store_true', help='Print file size in MB and exit.')
    args = parser.parse_args()

    if args.dry_run:
        get_file_size()
    else:
        download_data()
