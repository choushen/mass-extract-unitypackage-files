import os
import sys
import subprocess
from unitypackage_extractor.extractor import extractPackage
import re
import shutil
import zipfile

# Set the directory to search for .unitypackage files
# e.g. C:\Users\<your username>\AppData\Roaming\Unity\Asset Store-5.x
directory_path = r'<insert root folder containing .unitypackage files, or folder containing sub directories that contain .unitypackage files>'

# Create a folder on the desktop called "extracted-unity-assets" if it doesn't already exist
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
extracted_assets_path = os.path.join(desktop_path, "extracted-unity-assets")
if not os.path.exists(extracted_assets_path):
    os.makedirs(extracted_assets_path)

# Get the total number of .unitypackage files to extract
total_files = sum(len(files) for _, _, files in os.walk(directory_path) if any(file.endswith(".unitypackage") for file in files))
current_file = 0

# Loop through all files in the directory and subdirectories
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".unitypackage"):
            file_path = os.path.join(root, file)
            try:
                # Create a folder with the same name as the .unitypackage file in kebab case format within the "extracted-unity-assets" folder
                folder_name = re.sub(r'\W+', '-', os.path.splitext(file)[0].lower())
                folder_path = os.path.join(extracted_assets_path, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Extract the contents of the .unitypackage file into the folder
                subprocess.run(["python", "-m", "unitypackage_extractor", file_path, folder_path], check=True)

                # Zip up the contents of the folder
                zip_path = os.path.join(extracted_assets_path, folder_name + ".zip")
                with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            zip_file.write(file_path, os.path.relpath(file_path, folder_path))

                # Delete the kebab case folder
                shutil.rmtree(folder_path)

                # Update the progress bar
                current_file += 1
                progress = int((current_file / total_files) * 100)
                sys.stdout.write("\rExtracting files... [{0}%]".format(progress))
                sys.stdout.flush()
            except subprocess.CalledProcessError as e:
                print("Error extracting {0}: {1}".format(file_path, e))

# Clear the progress bar
sys.stdout.write("\r")
sys.stdout.flush()

print("Extraction complete.")