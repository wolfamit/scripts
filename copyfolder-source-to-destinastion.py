import os
import shutil
from tqdm import tqdm  # Import tqdm for progress bar visualization

def copy_files_to_unique_folder(source_folder, destination_folder):
    """
    Function to copy all files from a source folder (including subdirectories) 
    to a single destination folder, preserving only the files.
    
    Parameters:
        source_folder (str): The path of the source directory.
        destination_folder (str): The path of the destination directory.
    """

    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    # List all files from source folder and its subdirectories
    all_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            all_files.append(os.path.join(root, file))  # Get full path of each file
    
    print(f"Total files found: {len(all_files)}")

    # Copy each file from source to destination
    for file in tqdm(all_files, desc="Copying files", unit="file"):
        try:
            shutil.copy(file, destination_folder)  # Copy file to the destination
            print(f"Copied: {file}")
        except Exception as e:
            print(f"Error copying {file}: {e}")  # Handle errors if a file can't be copied

if __name__ == "__main__":
    # Define source and destination directories
    source_folder = "/Volumes/FLASHDEVICE"  # Path of the source folder (USB drive)
    destination_folder = "/Volumes/FLASHDEVICE/fabricio"  # Target folder for copied files

    print("Starting file copy process...")
    copy_files_to_unique_folder(source_folder, destination_folder)
    print("File copy process completed.")
