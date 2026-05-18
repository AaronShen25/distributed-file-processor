# Distributed File Processing Platform

A cloud-based distributed file processing platform where users upload files, jobs are processed asynchronously by workers, and results are stored and tracked through AWS services.

## Current Progress

### Phase 1: Local File Conversion
Completed a full-stack PNG to JPG conversion system.

Features:
- React frontend for file upload
- Flask backend API
- PNG → JPG conversion using Pillow
- Automatic file download
- File validation for supported input types

### Phase 2: Cloud Storage Integration
Completed AWS S3 storage integration.

Features:
- Upload original PNG files to AWS S3
- Upload converted JPG files to AWS S3
- AWS credential management via environment variables
- Temporary local processing with cloud persistence

## Current Architecture

```text
Frontend (React)
    ↓
Flask API
    ↓
Temporary local storage
    ↓
AWS S3 (original upload)
    ↓
Image conversion (Pillow)
    ↓
AWS S3 (converted output)
    ↓
Frontend download
```

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- Flask
- Flask-CORS
- Pillow

### Cloud
- AWS S3
- boto3
- python-dotenv

## How to Run

### Backend

Create `backend/.env`:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
S3_BUCKET_NAME=your_bucket_name
```

Install dependencies and run:

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

### Phase 3
- DynamoDB job tracking
- Job IDs and status API
- Frontend polling for status

### Phase 4
- AWS SQS async queue
- Decouple upload from processing

### Phase 5
- Worker processing system
- Lambda or Docker workers

### Phase 6
- Retries
- Dead-letter queue
- Validation
- Idempotency
- Monitoring

### Phase 7
- Dashboard UI
- Upload history
- Progress indicators
- Multiple file support