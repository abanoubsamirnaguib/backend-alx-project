FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project
COPY . .

# Create staticfiles and media directories
RUN mkdir -p /app/staticfiles /app/media/categories /app/media/food_types /app/media/ingredients

# Set proper permissions for media files
RUN chmod -R 755 /app/media

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Expose port (Railway uses PORT environment variable)
EXPOSE 8000

# Start the application with entrypoint
CMD ["./entrypoint.sh"]
