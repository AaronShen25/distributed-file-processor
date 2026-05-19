import os
import uuid
import boto3

from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, abort, request, send_file
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename

# Load AWS credentials and configuration from backend/.env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

ALLOWED_EXTENSIONS = {".png"}
OUTPUT_FORMAT = "JPEG"
OUTPUT_EXTENSION = ".jpg"

S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
S3_REGION = os.getenv('AWS_REGION')

# AWS S3 client used for file storage
s3_client = boto3.client(
    's3',
    region_name=S3_REGION,
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "Backend is running"


@app.route("/convert", methods=["POST"])
def convert():
    # Get uploaded file from frontend form submission
    uploaded_file = request.files.get("file")

    if not uploaded_file:
        abort(400, "File is required")

    # Sanitize filename to avoid unsafe characters/paths
    original_name = secure_filename(uploaded_file.filename)

    if original_name == "":
        abort(400, "Uploaded file must have a valid filename")

    # Split filename into name + extension for validation/output naming
    base_name, extension = os.path.splitext(original_name)

    if extension.lower() not in ALLOWED_EXTENSIONS:
        abort(400, "Only PNG files are supported")

    unique_id = str(uuid.uuid4())
    input_filename = f"{unique_id}_{original_name}"
    output_filename = f"{unique_id}_{base_name}{OUTPUT_EXTENSION}"

    # Local temporary storage paths
    source_path = os.path.join(UPLOAD_FOLDER, input_filename)
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    # Cloud storage object paths inside S3 bucket
    upload_s3_key = f"uploads/{input_filename}"
    output_s3_key = f"outputs/{output_filename}"

    # Save locally first so the file can be processed
    uploaded_file.save(source_path)

    # Upload original, convert locally, then upload converted result
    try:
        upload_file_to_s3(source_path, upload_s3_key)
        convert_image_to_jpg(source_path, output_path)
        upload_file_to_s3(output_path, output_s3_key)
    except UnidentifiedImageError:
        abort(400, "Uploaded file is not a valid image")
    except Exception as error:
        abort(500, f"Conversion failed: {error}")

    return send_file(
        output_path,
        as_attachment=True,
        attachment_filename=output_filename
    )

def convert_image_to_jpg(source_path, output_path):
    # Open PNG, convert to RGB (JPEG-compatible), save as JPG
    with Image.open(source_path) as image:
        rgb_image = image.convert("RGB")
        rgb_image.save(output_path, format=OUTPUT_FORMAT)

def upload_file_to_s3(file_path, s3_key):
    # Upload local file to the configured S3 bucket
    if not S3_BUCKET_NAME:
        raise ValueError("S3 bucket name is not configured")
    
    s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)


if __name__ == "__main__":
    app.run(debug=True)