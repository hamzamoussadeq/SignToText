import os

# Define the directory containing the folders to be renamed
directory = './data'

# Iterate over each folder (assumed to be named 'A' to 'Z')
for i, folder_name in enumerate(sorted(os.listdir(directory))):
    # Generate the new folder name (0 to 25)
    new_folder_name = str(i)

    # Generate the paths for old and new folders
    old_path = os.path.join(directory, folder_name)
    new_path = os.path.join(directory, new_folder_name)

    # Rename the folder
    os.rename(old_path, new_path)
    print(f"Renamed {folder_name} to {new_folder_name}")
