import os
import boto3


class S3DirectoryClient:
  def __init__(self, aws_access_key_id, aws_secret_access_key, bucket_name):
    self.s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    self.bucket_name = bucket_name

  def upload(self, source, dest):
    '''Upload a file or directory to a path inside the bucket'''
    if (os.path.isdir(source)):
      self.upload_dir(source, dest)
    else:
      self.upload_file(source, dest)

  def upload_file(self, source, dest):
    '''Upload a single file to a path inside the bucket'''
    try:
      print(f'Uploading {source} to {dest}')
      self.s3.upload_file(source, self.bucket_name, dest)
    except FileNotFoundError:
      print(f'The file {source} was not found')

  def upload_dir(self, source, dest):
    '''Upload a directory to a path inside the bucket'''
    prefix = '' if dest == '' else dest + '/'
    prefix += os.path.basename(source) + '/'
    for root, dirs, files in os.walk(source):
      for name in files:
        dir_part = os.path.relpath(root, source)
        dir_part = '' if dir_part == '.' else dir_part + '/'
        file_path = os.path.join(root, name)
        blob_path = prefix + dir_part + name
        self.upload_file(file_path, blob_path)

  def download(self, source, dest):
    '''Download a file or directory to a path on the local filesystem'''
    if not dest:
      raise Exception('A destination must be provided')
    
    items = self.ls_files(source, recursive=True)
    if items:
			# if source is a directory, dest must also be a directory
      if not source == '' and not source.endswith('/'):
        source += '/'
      if not dest.endswith('/'):
        dest += '/'
      # append the directory name from source to the destination
      dest += os.path.basename(os.path.normpath(source)) + '/'
      os.makedirs(dest, exist_ok=True)
      
      items = [source + blob for blob in items]
      for item in items:
        blob_dest = dest + os.path.relpath(item, source)
        self.download_file(item, blob_dest)
    else:
      self.download_file(source, dest)

  def download_file(self, source, dest):
    '''Download a single file to a path on the local filesystem'''
    with open(dest, 'wb') as file:
      print(f'Downloading {source} to {dest}')
      self.s3.download_fileobj(self.bucket_name, source, file)

  def ls_files(self, path, recursive=False):
    '''List directories under a path, optionally recursively'''
    if not path == '' and not path.endswith('/'):
      path += '/'

    results = []
    try:
      obj_ls = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=path)
      if recursive:
        for obj in obj_ls['Contents']:
          results.append(os.path.relpath(obj.get('Key'), path))
      else:
        for obj in obj_ls['Contents']:
          if obj['Key'] != path and '/' not in obj['Key'][len(path):]:
            results.append(os.path.relpath(obj.get('Key'), path))
    except KeyError:
      print(f'The directory {path} was not found')
    return results

  def ls_dirs(self, path, recursive=False):
    '''List directories under a path, optionally recursively'''
    dirs = []
    obj_ls = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=path)

    for obj in obj_ls['Contents']:
      item_parh = os.path.relpath(obj.get('Key'), path)
      _dir = os.path.dirname(item_parh)
      if _dir != "" and _dir != ".":
        if recursive:
          dirs.append(_dir)
        else:
          dirs.append(_dir.split("/")[0])

    return list(set(dirs))

  def rm(self, path, recursive=False):
    '''Remove a single file, or remove a path recursively'''
    if recursive:
      self.rmdir(path)
    else:
        print(f'Deleting {path}')
        self.s3.delete_object(Bucket=self.bucket_name, Key=path)

  def rmdir(self, path):
    '''Remove a directory and its contents recursively'''
    try:
      files = self.ls_files(path, recursive=True)
      for file in files:
        abs_path = os.path.join(path, file)
        print(f'Deleting {abs_path}')
        self.s3.delete_object(Bucket=self.bucket_name, Key=abs_path)
    except KeyError:
      print(f'The directory {path} was not found')