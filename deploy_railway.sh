#!/bin/bash
# Deploy script for Railway

echo "🚀 Deploying to Railway..."

# Check if we have the railway CLI
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Please install it first:"
    echo "npm install -g @railway/cli"
    exit 1
fi

# Login to Railway (if needed)
echo "🔑 Checking Railway authentication..."
railway whoami || railway login

# Link to project (if not already linked)
echo "🔗 Linking to Railway project..."
railway link

# Set essential environment variables
echo "⚙️  Setting environment variables..."

# Set DEBUG to False for production
railway variables set DEBUG=False

# Set a secure secret key (you should generate a new one)
if ! railway variables get SECRET_KEY &> /dev/null; then
    echo "🔐 Generating SECRET_KEY..."
    SECRET_KEY=$(python generate_secret_key.py)
    railway variables set SECRET_KEY="$SECRET_KEY"
fi

# Set allowed hosts
railway variables set ALLOWED_HOSTS="backend-alx-project-production.up.railway.app,.railway.app,.up.railway.app,localhost,127.0.0.1"

# Set CORS origins
railway variables set CORS_ALLOWED_ORIGINS="https://frontend-alx-project-2-fkiq6shrx-abanoubsamirnaguibs-projects.vercel.app,http://localhost:3000,http://127.0.0.1:3000"

# Deploy
echo "🚀 Deploying..."
railway up

echo "✅ Deployment complete!"
echo "🌐 Your app should be available at: https://backend-alx-project-production.up.railway.app"
echo "🏥 Health check: https://backend-alx-project-production.up.railway.app/api/health/"
echo "👤 Admin panel: https://backend-alx-project-production.up.railway.app/admin/"