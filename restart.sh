#!/bin/bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d

echo "Containers restarted successfully!"
echo "log zoom_django_1......"
docker logs zoom_django_1

echo "log zoom_flask-sock-connection_1......"
docker logs zoom_socketio_1