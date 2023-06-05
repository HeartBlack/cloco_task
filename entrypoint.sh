#!/bin/sh
cd backend/
echo "================================ Sever is starting now  =================================="

uvicorn wsgi:app --reload --workers 1 --host 0.0.0.0 --port 8000