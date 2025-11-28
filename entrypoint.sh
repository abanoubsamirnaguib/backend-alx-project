#!/bin/bash
set -e

# Set default port if PORT environment variable is not set
PORT=${PORT:-8000}

# Wait for database to be ready
echo "Waiting for database..."
sleep 5

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py createsuperuser_auto

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Starting server on port $PORT..."
# Replace the bind parameter with the correct port
exec "${@/0.0.0.0:8000/0.0.0.0:$PORT}"