from switch import StorageType
from config import STORAGE_CONFIG


def main():
  # Switch bewtween 's3' or 'blob'
  storage = StorageType('s3', STORAGE_CONFIG)
  client = storage.get_client()

  # Your code here...
  # Use any methods to list, upload, download or remove
  # any file or directory. Both (s3 and blob) work exactly the same.
  ls_files = client.ls_files('images/2024', recursive=False); print(ls_files)
  ls_dirs = client.ls_dirs('images', recursive=False); print(ls_dirs)
  client.download_file('images/2024/myimage.jpg', './myimage.jpg')
  client.download('images/2024/myimage.jpg', './myimage.jpg')
  client.download('images/2024', './')
  client.upload_file('./myimage.jpg', 'images/2024/myimage.jpg')
  client.upload('./myimage.jpg', 'images/2024/myimage.jpg')
  client.upload_dir('./2024', 'images')
  client.upload('./2024', 'images')
  # WARNING: Be careful! You can delete entire directories!
  client.rm('images/2024/myimage.jpg')
  client.rm('images/2024', recursive=True)
  client.rmdir('images/2024') # recursive always


if __name__ == '__main__':
  main()