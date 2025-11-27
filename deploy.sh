#!/bin/bash

# Fly.io deployment script for ALX Nexus E-commerce Backend

echo "🚀 Deploying ALX Nexus E-commerce Backend to Fly.io..."

# Check if fly CLI is installed
if ! command -v fly &> /dev/null; then
    echo "❌ Fly CLI is not installed. Please install it first:"
    echo "   Visit: https://fly.io/docs/hands-on/install-flyctl/"
    exit 1
fi

# Check if logged in to Fly.io
if ! fly auth whoami &> /dev/null; then
    echo "❌ Not logged in to Fly.io. Please run 'fly auth login' first."
    exit 1
fi

echo "✅ Fly CLI is installed and authenticated"

# Create the app if it doesn't exist
echo "📝 Creating or updating Fly.io app..."
if ! fly apps list | grep -q "alx-project-nexus-ecommerce"; then
    echo "Creating new app: alx-project-nexus-ecommerce"
    fly apps create alx-project-nexus-ecommerce
else
    echo "App already exists: alx-project-nexus-ecommerce"
fi

# Generate a strong secret key for production
echo "🔐 Generating Django secret key..."
SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")

# Set required secrets
echo "🔧 Setting required environment variables..."
fly secrets set SECRET_KEY="$SECRET_KEY" --app alx-project-nexus-ecommerce
fly secrets set DEBUG=False --app alx-project-nexus-ecommerce
fly secrets set ALLOWED_HOSTS="alx-project-nexus-ecommerce.fly.dev,.fly.dev" --app alx-project-nexus-ecommerce

# Create and attach PostgreSQL database
echo "🗄️ Setting up PostgreSQL database..."
if ! fly postgres list | grep -q "alx-project-nexus-ecommerce-db"; then
    echo "Creating new PostgreSQL database..."
    fly postgres create --name alx-project-nexus-ecommerce-db --region iad --initial-cluster-size 1
    fly postgres attach alx-project-nexus-ecommerce-db --app alx-project-nexus-ecommerce
else
    echo "PostgreSQL database already exists"
fi

# Create persistent volume for media files
echo "💾 Creating persistent volume for media files..."
if ! fly volumes list | grep -q "project_nexus_data"; then
    fly volumes create project_nexus_data --region iad --size 1 --app alx-project-nexus-ecommerce
else
    echo "Volume already exists"
fi

# Deploy the application
echo "🚀 Deploying application..."
fly deploy

echo "✅ Deployment completed!"
echo ""
echo "📋 Next steps:"
echo "1. Check app status: fly status --app alx-project-nexus-ecommerce"
echo "2. View logs: fly logs --app alx-project-nexus-ecommerce"
echo "3. Open app: fly open --app alx-project-nexus-ecommerce"
echo "4. Set CORS origins if needed:"
echo "   fly secrets set CORS_ALLOWED_ORIGINS='https://your-frontend-domain.com' --app alx-project-nexus-ecommerce"
echo ""
echo "🌐 Your app will be available at: https://alx-project-nexus-ecommerce.fly.dev"