import os

import boto3
import mediapipe as mp
from botocore.exceptions import ClientError

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_REGION = os.environ["AWS_REGION"]
AWS_S3_BUCKET_NAME = os.environ["AWS_S3_BUCKET_NAME"]

client = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION
                      )
bucket = AWS_S3_BUCKET_NAME


def load_img(img_key):
    filename = download_img(img_key)
    return mp.Image.create_from_file(filename)


def download_img(img_key):
    file_name = "image/" + img_key.split("/")[1]
    try:
        client.download_file(bucket, img_key, file_name)

        print(f"Download file: {file_name}")
        return file_name
    except ClientError as e:
        return file_name


def delete_img(img_key):
    file_name = "image/" + img_key.split("/")[1]
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"Deleted file: {file_name}")
        else:
            print(f"File {file_name} does not exist")
    except Exception as e:
        print(f"Error deleting file {file_name}: {e}")
