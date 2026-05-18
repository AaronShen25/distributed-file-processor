# Phase 2: AWS S3 Storage Integration

## Goal

Replace local-only file storage with AWS S3 cloud storage while keeping the existing PNG to JPG conversion workflow functional.

## What Was Added

- AWS account setup
- IAM user with programmatic access
- S3 bucket configuration
- boto3 integration
- environment-based credential loading
- backend S3 upload helper

## Current Flow

```text
1. User uploads PNG from frontend
2. Flask backend receives file
3. File is saved temporarily to local uploads/
4. Original PNG is uploaded to S3
5. Image is converted locally to JPG
6. Converted JPG is saved temporarily to local outputs/
7. Converted JPG is uploaded to S3
8. Backend returns JPG to frontend for download
```

## Design Decisions

### Why temporary local storage?

Full cloud-native async processing is planned for later phases.

For Phase 2, temporary local storage keeps the existing conversion logic simple while introducing cloud persistence.

### Why S3 now?

S3 separates storage from application logic and prepares the system for distributed worker processing in later phases.

## Limitations

Current limitations:

- processing still happens synchronously inside Flask
- frontend still receives immediate download
- local temporary files are still created
- no cleanup of temporary files yet
- no job tracking
- no async queue

## Next Phase

Phase 3 introduces:

- job creation
- DynamoDB status tracking
- status polling endpoints
- frontend status updates