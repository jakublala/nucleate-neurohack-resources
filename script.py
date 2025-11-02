#!/usr/bin/env python

"""
A CLI script to download all NeuroHack dataset notebooks
from the NeuromatchAcademy GitHub repository.

This script requires the 'requests' library:
    pip install requests

Usage:
    python script.py

This will download all 26 notebooks to the current directory.
"""

import os
import requests
from urllib.parse import urlparse

# --- 1. All 26 Colab Notebook URLs ---
COLAB_URLS = [
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/IBL_BWM_Neuromatch_tutorial.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/IBL_ONE_tutorial.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/visual_learning_80k_neurons.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_pre_processed_file.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/neurons/load_Allen_Visual_Behavior_from_SDK.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_hcp_task_with_behaviour.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_hcp_task.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_hcp.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_fslcourse.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_hcp_retino.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_kay_images.ipynb",
    "https://colab.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_bonner_navigational_affordances.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_cichy_fMRI_MEG.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/fMRI/load_algonauts_videos.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/exploreAJILE12.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_faceshouses.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_fingerflex.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_joystick_track.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_memory_nback.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/ECoG/load_ECoG_motor_imagery.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/behavior_and_theory/Loading_CalMS21_data.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/behavior_and_theory/IBL_behavior_data.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/behavior_and_theory/laquitaine_human_errors.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/behavior_and_theory/laquitaine_motion_prior_learning.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/behavior_and_theory/RNN_working_memory.ipynb",
    "https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/main/projects/behavior_and_theory/motor_RNNs.ipynb"
]

# --- 2. Configuration: GitHub Repository ---
REPO_OWNER = "NeuromatchAcademy"
REPO_NAME = "course-content"
BRANCH = "main"
BASE_RAW_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/"

class Downloader:
    """A CLI tool to download NeuroHack notebooks."""

    def _get_paths(self):
        """
        Parses the Colab URLs to extract the raw GitHub paths and filenames.
        Returns a dictionary: { 'filename.ipynb': 'full/path/in/repo.ipynb' }
        """
        notebook_paths = {}
        
        # Define the parts of the URL to remove
        github_path_prefix = f"/github/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/"
        
        for url in COLAB_URLS:
            try:
                parsed_url = urlparse(url)
                # Find the start of the relevant GitHub path
                path_start_index = parsed_url.path.find(github_path_prefix)
                if path_start_index == -1:
                    print(f"Warning: Could not parse path from URL: {url}")
                    continue
                
                # Extract the repo path
                repo_path = parsed_url.path[path_start_index + len(github_path_prefix):]
                # Get the filename
                filename = os.path.basename(repo_path)
                
                notebook_paths[filename] = repo_path
                
            except Exception as e:
                print(f"Error parsing URL {url}: {e}")
                
        return notebook_paths

    def run(self):
        """
        Downloads all configured notebooks to the current working directory.
        """
        save_directory = os.getcwd()
        print(f"Parsing {len(COLAB_URLS)} Colab URLs...")
        
        notebook_paths = self._get_paths()
        
        print(f"Found {len(notebook_paths)} notebooks to download.")
        print(f"Saving files to: {save_directory}\n")
        
        download_count = 0
        fail_count = 0
        
        for filename, repo_path in notebook_paths.items():
            
            download_url = BASE_RAW_URL + repo_path
            save_path = os.path.join(save_directory, filename) # Save to current dir
            
            try:
                print(f"Downloading: {filename}...")
                response = requests.get(download_url)
                
                # Check for errors (like 404 Not Found)
                response.raise_for_status()
                
                # Save the notebook content to a file
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                    
                print(f"  SUCCESS: Saved to {save_path}")
                download_count += 1
                
            except requests.RequestException as e:
                print(f"  FAILED:  {filename} - {e}")
                print(f"           (URL: {download_url})")
                fail_count += 1

        print("\n" + "---" * 10)
        print("Download Summary")
        print("---" * 10)
        print(f"Successfully downloaded: {download_count}")
        print(f"Failed to download:    {fail_count}")
        print("\nDownload script finished.")

if __name__ == "__main__":
    downloader = Downloader()
    downloader.run()