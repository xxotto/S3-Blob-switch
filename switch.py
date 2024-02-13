from storages import BlobDirectoryClient, S3DirectoryClient


class StorageType:
  def __init__(self, storage_type, storage_cfg):
    self.storage_type = storage_type
    self.storage_cfg = storage_cfg

  def get_client(self):
    if self.storage_type == 'blob':
      return BlobDirectoryClient(
        self.storage_cfg['BLOB_CONFIG']['CONNECTION_STRING'],
        self.storage_cfg['BLOB_CONFIG']['CONTAINER'],
      )
    elif self.storage_type == 's3':
      return S3DirectoryClient(
        self.storage_cfg['S3_CONFIG']['ACCESS_KEY_ID'],
        self.storage_cfg['S3_CONFIG']['SECRET_ACCESS_KEY'],
        self.storage_cfg['S3_CONFIG']['BUCKET_NAME'],
      )
    else:
      raise ValueError("Invalid argument (select 'blob' or 's3'). ")