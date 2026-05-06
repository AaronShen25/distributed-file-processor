# Distributed File Processing Platform

A cloud-based distributed file processing platform where users upload files, jobs are processed asynchronously by workers, and results are stored and tracked through AWS services.

## Phase 1: Local File Conversion

Completed a full-stack local PNG to JPG converter.

### Features

- Upload PNG file through React frontend
- Send file to Flask backend
- Convert PNG → JPG using Pillow
- Automatically download converted image
- Basic file validation

## Phase 2: AWS S3 Storage

Next phase: move uploaded and converted files from local folders into AWS S3.

### Phase 2 Goals

- Create an S3 bucket for file storage
- Upload original PNG files to S3
- Upload converted JPG files to S3
- Generate download links for converted files
- Keep local conversion logic working while replacing local storage with cloud storage

## Tech Stack

- Frontend: React + Vite
- Backend: Flask + Python
- Image Processing: Pillow
- Phase 2 Cloud Storage: AWS S3

## How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Future Phases

- DynamoDB job tracking
- SQS async queue
- Worker processing with Lambda or Docker
- Reliability features: retries, validation, dead-letter queue
- Simple dashboard