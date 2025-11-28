#!/usr/bin/env python3
"""
Script to update CORS settings for production deployment
"""
import os
import sys

def update_railway_env():
    """Update environment variables for Railway deployment"""
    print("🔧 Setting up CORS environment variables for Railway...")
    
    # The domains that should be allowed
    frontend_domains = [
        'https://frontend-alx-project-2-fkiq6shrx-abanoubsamirnaguibs-projects.vercel.app',
        'http://localhost:3000',
        'http://127.0.0.1:3000',
        'http://localhost:5173',
        'http://127.0.0.1:5173'
    ]
    
    cors_origins = ','.join(frontend_domains)
    
    print(f"CORS_ALLOWED_ORIGINS should be set to:")
    print(cors_origins)
    print()
    print("To update Railway environment variables:")
    print("1. Go to your Railway project dashboard")
    print("2. Navigate to Variables tab")
    print("3. Add or update these variables:")
    print(f"   CORS_ALLOWED_ORIGINS = {cors_origins}")
    print("   CORS_ALLOW_ALL_ORIGINS = False")
    print("4. Redeploy your service")
    
    return cors_origins

if __name__ == "__main__":
    update_railway_env()