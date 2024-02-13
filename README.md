# S3-Blob-switch

This repository contains a class called `StorageType()` that allows easy switching between **Azure Blob Storage** and **S3 buckets** (or vice versa) using an input string of `'s3'` or `'blob'`.

Assuming you already know how to migrate your files from one cloud to another (if not check [rclone](https://rclone.org/)), you can use `StorageType()` to **list**, **upload**, **download**, and **remove** files and directories within either of the two storage systems.

Or simply use the class that creates the **S3 client** (`S3DirectoryClient`) or the **blob client** (`BlobDirectoryClient`) individually from `storage/s3_storage.py` or `storage/blob_storage.py`, respectively.

## Usage

1. Clone this repo.
```bash
git clone https://github.com/xxotto/S3-Blob-switch
cd S3-Blob-switch
```

2. Install `requirements.txt`.
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Add your own S3 Buckets and Blob Storage keys to `.env` file.

4. Review and modify the `main.py` file and add the methods to your client as desired.

5. Run the `main.py` code with your changes and new methods, and if you want to switch storage types, modify the input string in the `StorageType()` class.

## Future Developments

- Look for functions or methods from the azure-storage or boto3 libraries to avoid unnecessary iteration over all files.

- Explore alternatives to avoid manual handling of paths.
