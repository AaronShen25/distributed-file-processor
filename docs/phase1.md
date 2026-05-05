# Phase 1: Local File Conversion

## Overview

Phase 1 implements a full end-to-end system for converting PNG images to JPG.

The system consists of a React frontend and a Flask backend.

## Flow

1. User selects a PNG file in the frontend  
2. Frontend sends a POST request to `/convert`  
3. Backend:
   - validates the file
   - saves it to `uploads/`
   - converts it using Pillow
   - saves the result to `outputs/`
4. Backend returns the converted JPG  
5. Frontend automatically downloads the file  

## Key Components

- Flask API (`/convert`)
- Pillow image processing
- React frontend with file upload and fetch request

## Notes

- Only PNG → JPG is supported  
- Files are stored locally  