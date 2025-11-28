#!/bin/bash

# Railway deployment debug script
echo "=== Railway Deployment Diagnostics ==="
echo "Date: $(date)"
echo "Python version: $(python --version)"
echo "Django version: $(python -c 'import django; print(django.get_version())')"
echo

echo "=== Environment Variables ==="
echo "PORT: ${PORT:-'Not set'}"
echo "DEBUG: ${DEBUG:-'Not set'}"
echo "DATABASE_URL: ${DATABASE_URL:0:20}..." # Show only first 20 chars for security
echo "SECRET_KEY: ${SECRET_KEY:0:10}..." # Show only first 10 chars for security
echo

echo "=== Database Connection ==="
python manage.py check --database default
echo

echo "=== Static Files ==="
python manage.py collectstatic --noinput --verbosity=2
echo

echo "=== Migrations ==="
python manage.py migrate --verbosity=2
echo

echo "=== Health Check ==="
python manage.py check
echo

echo "=== Starting Server ==="