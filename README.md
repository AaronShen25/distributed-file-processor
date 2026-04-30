# Distributed File Processing Platform

A cloud-based distributed file processing platform where users upload files, jobs are processed asynchronously by workers, and results are stored and tracked through AWS services.

## Phase 1 Goal
Build a basic local file converter:
- Upload file
- Convert PNG → JPG
- Download processed result

## Future Phases
- AWS S3 cloud storage
- DynamoDB job tracking
- SQS async queue
- Worker processing with Lambda or Docker
- Reliability features (retries, validation, DLQ)
- Simple dashboard