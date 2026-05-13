import os
import boto3
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

s3 = boto3.client(
    's3',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
)

bucket_name = os.getenv('S3_BUCKET_NAME')

s3.put_object(
    Bucket=bucket_name,
    Key='test-file.txt',
    Body='This is a test file for S3 upload.'
)

print(f"File 'test-file.txt' uploaded to bucket '{bucket_name}' successfully.")