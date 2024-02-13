from dotenv import load_dotenv
from os import environ

load_dotenv()

STORAGE_CONFIG = {
  'BLOB_CONFIG' : {
    'CONNECTION_STRING': environ.get('BLOB_CONNECTION_STRING'),
    'CONTAINER': environ.get('BLOB_CONTAINER'),
    },
  'S3_CONFIG' : {
    'ACCESS_KEY_ID': environ.get('S3_ACCESS_KEY_ID'),
    'SECRET_ACCESS_KEY': environ.get('S3_SECRET_ACCESS_KEY'),
    'BUCKET_NAME': environ.get('S3_BUCKET_NAME'),
  }
}