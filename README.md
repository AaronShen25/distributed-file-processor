# Distributed File Processing Platform

A cloud-based distributed file processing platform where users upload files, jobs are processed asynchronously by workers, and results are stored and tracked through AWS services.

## Phase 1 (Current)

Implemented a full-stack local file conversion system:

- Upload PNG file through a React frontend  
- Backend processes file using Flask and Pillow  
- Convert PNG → JPG  
- Automatically download the converted image  

## Tech Stack

- Frontend: React (Vite)  
- Backend: Flask (Python)  
- Image Processing: Pillow  

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

- AWS S3 cloud storage  
- DynamoDB job tracking  
- SQS async queue  
- Worker processing with Lambda or Docker  
- Reliability features (retries, validation, DLQ)  
- Simple dashboard  