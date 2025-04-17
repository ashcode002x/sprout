#!/bin/bash

# Create required directories if they don't exist
mkdir -p backend/logs
mkdir -p flask-sock-connection/logs

# Build and start containers
docker-compose up -d

# Create superuser
docker-compose exec django python manage.py createsuperuser

echo "Setup completed successfully!"
echo "Django app is running at http://localhost:8000"
echo "Socket.IO server is running at http://localhost:5000"
echo "PostgreSQL is available at localhost:5432"