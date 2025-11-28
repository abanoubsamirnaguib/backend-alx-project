# Railway Deployment Issues & Solutions

## Current Issues

1. **404 Not Found at root URL** - FIXED ✅
2. **500 Error on Admin Panel** - INVESTIGATING 🔍

## Solutions Applied

### 1. Fixed Root URL 404 Error
- Added home view in `config/urls.py` that provides navigation links
- Now `https://backend-alx-project-production.up.railway.app/` shows a simple homepage

### 2. Fixed Docker Configuration
- Updated `Dockerfile` to properly handle Railway's PORT environment variable
- Fixed `entrypoint.sh` to start gunicorn correctly with the dynamic port
- Added proper workers and timeout configuration

### 3. Enhanced Static Files Handling
- Added WhiteNoise configuration for better static file serving
- Ensured static files are collected properly during deployment

## Debugging the Admin 500 Error

The admin panel error could be caused by:

1. **Missing Static Files**: Django admin requires CSS/JS files
2. **Database Issues**: Missing migrations or connection problems
3. **Secret Key Issues**: Invalid or missing SECRET_KEY

### Steps to Debug:

1. **Check Health Endpoint**:
   ```
   https://backend-alx-project-production.up.railway.app/api/health/
   ```
   This will show database connectivity and basic app status.

2. **Enable Debug Mode Temporarily**:
   In Railway dashboard, set environment variable:
   ```
   DEBUG=True
   ```
   This will show detailed error messages.

3. **Check Railway Logs**:
   ```bash
   railway logs
   ```

## Required Environment Variables in Railway

Set these in your Railway project dashboard:

```env
# Security
SECRET_KEY=your-secret-key-here
DEBUG=False

# Database (Railway should auto-provide DATABASE_URL)
DATABASE_URL=postgresql://...

# Hosts
ALLOWED_HOSTS=backend-alx-project-production.up.railway.app,.railway.app,.up.railway.app

# CORS
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com,http://localhost:3000

# Superuser (optional)
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com  
DJANGO_SUPERUSER_PASSWORD=your-secure-password
```

## Deployment Commands

1. **Using Railway CLI**:
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login and link project
   railway login
   railway link
   
   # Deploy
   railway up
   ```

2. **Manual GitHub Integration**:
   - Connect your GitHub repo to Railway
   - Set environment variables in Railway dashboard
   - Push to main branch to auto-deploy

## Testing Endpoints

After deployment, test these URLs:

1. **Home**: `https://backend-alx-project-production.up.railway.app/`
2. **Health Check**: `https://backend-alx-project-production.up.railway.app/api/health/`
3. **API Root**: `https://backend-alx-project-production.up.railway.app/api/`
4. **Admin** (after fixing): `https://backend-alx-project-production.up.railway.app/admin/`

## Next Steps to Fix Admin

1. Check the health endpoint first to confirm database connectivity
2. If database is working, temporarily enable DEBUG=True to see the exact error
3. Check Railway logs for any migration or static file collection errors
4. Ensure the superuser creation command runs successfully

## Common Railway Deployment Issues

1. **Port Binding**: Fixed in our entrypoint.sh
2. **Static Files**: Fixed with WhiteNoise configuration  
3. **Database URL**: Railway auto-provides this
4. **Environment Variables**: Must be set in Railway dashboard
5. **File Permissions**: Fixed in Dockerfile with chmod

The root URL issue is now fixed. The admin 500 error needs investigation with the steps above.