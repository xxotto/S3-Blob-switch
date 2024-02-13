from itertools import islice
from switch import StorageType
from config import STORAGE_CONFIG


def main():
  BlobDirClient = StorageType('blob', STORAGE_CONFIG)
  S3DirClient = StorageType('s3', STORAGE_CONFIG)

  bl_client = BlobDirClient.get_client()
  s3_client = S3DirClient.get_client()


  # ============ List files ============
  path = 'user/project/'

  # List items (Recursive)
  ls_items_bl = bl_client.ls_files(path, recursive=True)
  ls_items_s3 = s3_client.ls_files(path, recursive=True)
  print(f'\n- List items (Recursive) in {path}')
  for i, filename in islice(enumerate(zip(sorted(ls_items_bl), sorted(ls_items_s3))), 5):
    print( i, 'blob', filename[0])
    print( i, 'aws ', filename[1])

  # List items (Non recursive)
  ls_items_bl = bl_client.ls_files(path)
  ls_items_s3 = s3_client.ls_files(path)
  print(f'\n- List items (Non recursive) in {path}')
  for i, filename in islice(enumerate(zip(sorted(ls_items_bl), sorted(ls_items_s3))), 5):
    print( i, 'blob', filename[0])
    print( i, 'aws ', filename[1])

  # List directories (Recursive)
  ls_dirs_bl = bl_client.ls_dirs(path, recursive=True)
  ls_dirs_s3 = s3_client.ls_dirs(path, recursive=True)
  print(f'\n- List directories (Recursive) in {path}')
  for i, _dir in islice(enumerate(zip(sorted(ls_dirs_bl), sorted(ls_dirs_s3))), 5):
    print('blob', i, _dir[0])
    print('aws ', i, _dir[1])

  # List of directories (Non recursive)
  ls_dirs_bl = bl_client.ls_dirs(path);
  ls_dirs_s3 = s3_client.ls_dirs(path)
  print(f'\n- List of directories (Non recursive) in {path}')
  for i, _dir in islice(enumerate(zip(sorted(ls_dirs_bl), sorted(ls_dirs_s3))), 5):
    print( i, 'blob', _dir[0])
    print( i, 'aws ', _dir[1])


  # ============ Download ============
  # Dowload file
  file_path = 'user/project/images/DJI_0842.JPG'
  file_dest = './DJI_0842.JPG'
  #bl_client.download_file(file_path, file_dest)
  #s3_client.download_file(file_path, file_dest)
  #bl_client.download(file_path, file_dest)
  #s3_client.download(file_path, file_dest)

  # Dowload directory (recursive always)
  dir_path = 'user/project/images'
  dir_dest = './'
  #bl_client.download(dir_path, dir_dest)
  #s3_client.download(dir_path, dir_dest)


  # ============ Upload ============
  # Upload file
  file_path = './DJI_0842.JPG'
  file_dest = 'user/project/DJI_0842.JPG'
  #bl_client.upload_file(file_path, file_dest)
  #bl_client.upload(file_path, file_dest)
  #s3_client.upload_file(file_path, file_dest)
  #s3_client.upload(file_path, file_dest)

  # Upload directory (recursive always)
  dir_path = './images'
  dir_dest = 'user/project/images_inf'
  #bl_client.upload_dir(dir_path, dir_dest)
  #bl_client.upload(dir_path, dir_dest)
  #s3_client.upload_dir(dir_path, dir_dest) 
  #s3_client.upload(dir_path, dir_dest)


  # ============ Remove ============
  # Remove file
  file_path = 'user/project/images_inf/images/DJI_0842.JPG'
  #bl_client.rm(file_path)
  #s3_client.rm(file_path)

  # Remove directory
  dir_path = 'user/project/images_inf/images'
  #bl_client.rmdir(dir_path)
  #bl_client.rm(dir_path, recursive=True)
  #s3_client.rmdir(dir_path)
  #s3_client.rm(dir_path, recursive=True)


if __name__ == '__main__':
  main()