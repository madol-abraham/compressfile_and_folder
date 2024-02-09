#!/usr/bin/python3
''' Python program that allows users to compress files and folders.'''

import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    folder_name = os.path.basename(folder_path)
    current_date = datetime.now().strftime("%Y_%m_%d")
    compressed_file_name = f"{folder_name}_{current_date}.{compress_type}"

    try:
        if compress_type == "zip":
            with zipfile.ZipFile(compressed_file_name, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), start=folder_path))

        elif compress_type == "tar":
            with tarfile.open(compressed_file_name, 'w') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))

        elif compress_type == "tgz":
            with tarfile.open(compressed_file_name, 'w:gz') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))

        print(f"Compression successful! Compressed file saved as '{compressed_file_name}'")
    except Exception as e:
        print(f"Compression failed: {e}")

if __name__ == '__main__':
    folder_path = input("Enter the path of the folder to compress: ")
    compress_types = ["zip", "tar", "tgz"]
    print("Available compress types:", ", ".join(compress_types))
    compress_type = input('Enter the desired compress type: ')

    if compress_type in compress_types:
        compress_folder(folder_path, compress_type)
    else:
        print("Invalid compress type. Please select from the available options.")

