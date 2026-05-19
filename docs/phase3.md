# Phase 3: Job Tracking with DynamoDB

## Goal

Introduce persistent job tracking so file processing is represented as jobs rather than immediate one-off conversions.

## Planned Changes

- Create DynamoDB table for job metadata
- Generate unique job IDs
- Store job status information
- Add backend endpoints for job creation and lookup

## Planned Flow

```text
1. User uploads file
2. Backend creates job record in DynamoDB
3. Job status = pending
4. Backend uploads file to S3
5. Job status = processing
6. Backend converts image
7. Converted file uploaded to S3
8. Job status = completed
9. Frontend can query job status
```

## Job Schema

Example:

```json
{
  "job_id": "uuid",
  "status": "processing",
  "input_s3_key": "uploads/file.png",
  "output_s3_key": "outputs/file.jpg",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "error_message": null
}
```

## Purpose

This phase prepares the system for asynchronous distributed workers in later phases.