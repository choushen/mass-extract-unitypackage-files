# Mass Extract Unitypackage Extractor

This Python script extracts the contents of all `.unitypackage` files in a specified directory and its subdirectories. It uses the `unitypackage_extractor` package to extract the contents of each package into a folder with the same name as the package file, in kebab case format, within a folder called `extracted-unity-assets` on the desktop. It then zips up the contents of each folder.

## Requirements

- Python 3.x
- `unitypackage_extractor` package

## Usage

1. Set the `directory_path` variable in the script to the directory where your `.unitypackage` files are located.
2. Run the script using Python 3.x.
3. The extracted assets will be saved in a folder called `extracted-unity-assets` on your desktop, with each package's contents zipped up.

## Notes

- The script will create the `extracted-unity-assets` folder on your desktop if it doesn't already exist.
- The script will overwrite any existing folders with the same name as the `.unitypackage` file being extracted.
- The script will skip any files that are not `.unitypackage` files.
- The script will display progress information in the console as it extracts and zips up each package.

