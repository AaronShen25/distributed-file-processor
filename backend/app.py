import os
import uuid
from flask import Flask, abort, request, send_file
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

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

    if original_name == "" or not original_name.lower().endswith(".png"):
        abort(400, "Only PNG files are supported")

    unique_id = str(uuid.uuid4())
    filename = f"{unique_id}_{original_name}"

    source_path = os.path.join(UPLOAD_FOLDER, filename)

    uploaded_file.save(source_path)

    output_name = filename.replace(".png", ".jpg")
    output_path = os.path.join(OUTPUT_FOLDER, output_name)

    with Image.open(source_path) as image:
        rgb_img = image.convert("RGB")
        rgb_img.save(output_path, format="JPEG")

    return send_file(output_path, as_attachment=True, attachment_filename=output_name)

if __name__ == "__main__":
    app.run(debug=True)