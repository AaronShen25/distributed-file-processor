import os
import uuid

from flask import Flask, abort, request, send_file
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

ALLOWED_EXTENSIONS = {".png"}
OUTPUT_FORMAT = "JPEG"
OUTPUT_EXTENSION = ".jpg"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "Backend is running"


@app.route("/convert", methods=["POST"])
def convert():
    uploaded_file = request.files.get("file")

    if not uploaded_file:
        abort(400, "File is required")

    original_name = secure_filename(uploaded_file.filename)

    if original_name == "":
        abort(400, "Uploaded file must have a valid filename")

    base_name, extension = os.path.splitext(original_name)

    if extension.lower() not in ALLOWED_EXTENSIONS:
        abort(400, "Only PNG files are supported")

    unique_id = str(uuid.uuid4())
    input_filename = f"{unique_id}_{original_name}"
    output_filename = f"{unique_id}_{base_name}{OUTPUT_EXTENSION}"

    source_path = os.path.join(UPLOAD_FOLDER, input_filename)
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    uploaded_file.save(source_path)

    try:
        convert_image_to_jpg(source_path, output_path)
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
    with Image.open(source_path) as image:
        rgb_image = image.convert("RGB")
        rgb_image.save(output_path, format=OUTPUT_FORMAT)


if __name__ == "__main__":
    app.run(debug=True)