@echo off
REM Fly.io deployment script for ALX Nexus E-commerce Backend (Windows)

echo 🚀 Deploying ALX Nexus E-commerce Backend to Fly.io...

REM Check if fly CLI is installed
where fly >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Fly CLI is not installed. Please install it first:
    echo    Visit: https://fly.io/docs/hands-on/install-flyctl/
    pause
    exit /b 1
)

echo ✅ Fly CLI is installed

REM Check if logged in to Fly.io
fly auth whoami >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Not logged in to Fly.io. Please run 'fly auth login' first.
    pause
    exit /b 1
)

echo ✅ Authenticated with Fly.io

REM Create the app if it doesn't exist
echo 📝 Creating or updating Fly.io app...
fly apps list | findstr "alx-project-nexus-ecommerce" >nul 2>nul
if %errorlevel% neq 0 (
    echo Creating new app: alx-project-nexus-ecommerce
    fly apps create alx-project-nexus-ecommerce
) else (
    echo App already exists: alx-project-nexus-ecommerce
)

REM Generate a strong secret key for production
echo 🔐 Generating Django secret key...
for /f "delims=" %%i in ('python generate_secret_key.py') do set SECRET_KEY=%%i

REM Set required secrets
echo 🔧 Setting required environment variables...
fly secrets set SECRET_KEY="%SECRET_KEY%" --app alx-project-nexus-ecommerce
fly secrets set DEBUG=False --app alx-project-nexus-ecommerce
fly secrets set ALLOWED_HOSTS="alx-project-nexus-ecommerce.fly.dev,.fly.dev" --app alx-project-nexus-ecommerce

REM Create and attach PostgreSQL database
echo 🗄️ Setting up PostgreSQL database...
fly postgres list | findstr "alx-project-nexus-ecommerce-db" >nul 2>nul
if %errorlevel% neq 0 (
    echo Creating new PostgreSQL database...
    fly postgres create --name alx-project-nexus-ecommerce-db --region iad --initial-cluster-size 1
    fly postgres attach alx-project-nexus-ecommerce-db --app alx-project-nexus-ecommerce
) else (
    echo PostgreSQL database already exists
)

REM Create persistent volume for media files
echo 💾 Creating persistent volume for media files...
fly volumes list | findstr "project_nexus_data" >nul 2>nul
if %errorlevel% neq 0 (
    fly volumes create project_nexus_data --region iad --size 1 --app alx-project-nexus-ecommerce
) else (
    echo Volume already exists
)

REM Deploy the application
echo 🚀 Deploying application...
fly deploy

echo ✅ Deployment completed!
echo.
echo 📋 Next steps:
echo 1. Check app status: fly status --app alx-project-nexus-ecommerce
echo 2. View logs: fly logs --app alx-project-nexus-ecommerce
echo 3. Open app: fly open --app alx-project-nexus-ecommerce
echo 4. Set CORS origins if needed:
echo    fly secrets set CORS_ALLOWED_ORIGINS="https://your-frontend-domain.com" --app alx-project-nexus-ecommerce
echo.
echo 🌐 Your app will be available at: https://alx-project-nexus-ecommerce.fly.dev
pause