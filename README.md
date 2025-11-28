# Custom Food Builder Application

A full-stack food ordering application where users can customize their meals using an interactive drag-and-drop interface. Features user authentication, order history, and reorder functionality.

## Tech Stack

### Backend
- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL (default) with SQLite fallback

### Frontend
- React 18
- Vite
- React Router
- Framer Motion (animations)

## Project Structure

```
custom_food_builder/
├── backend/
│   ├── config/          # Django project settings
│   ├── api/             # Main API app
│   │   ├── models.py    # Database models
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   └── manage.py
└── frontend/
    ├── src/
    │   ├── pages/       # React pages
    │   ├── App.jsx
    │   └── main.jsx
    └── package.json
```

## Production API

The backend is deployed on Railway and available at:
**Base URL**: `https://backend-alx-project-production.up.railway.app/api/`

Admin panel: `https://backend-alx-project-production.up.railway.app/admin/`

## Local Development Setup

### Backend Setup

1. Navigate to backend directory:
```cmd
cd custom_food_builder\backend
```

2. Install Python dependencies (now includes PostgreSQL driver):
```cmd
pip install -r requirements.txt
```

3. Run migrations:
```cmd
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser for admin access:
```cmd
python manage.py createsuperuser
```

5. Start the development server:
```cmd
python manage.py runserver
```

For local development, the backend will be available at `http://localhost:8000`
Local admin panel: `http://localhost:8000/admin`

### Frontend Setup

1. Navigate to frontend directory:
```cmd
cd custom_food_builder\frontend
```

2. Install dependencies:
```cmd
npm install
```

3. Start the development server:
```cmd
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Usage

### Admin Panel

1. Access the admin panel at `https://backend-alx-project-production.up.railway.app/admin/`
2. Login with your superuser credentials
3. Add Categories (e.g., "Savory", "Sweets", "Desserts")
4. Add Food Types under each category (e.g., "Burger", "Sandwich")
5. Add Ingredients for each Food Type with:
   - Name
   - Price
   - Image
   - Layer order (for visual stacking)
   - Is default (required ingredients)

### Customer Flow

1. Visit the landing page
2. Click "Start Building"
3. Select a category
4. Select a food type
5. Customize by clicking/dragging ingredients
6. Place order with delivery details

## API Endpoints

Base URL: `https://backend-alx-project-production.up.railway.app/api/`

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and receive JWT tokens
- `GET /api/auth/profile/` - Get current user profile (requires authentication)
- `POST /api/auth/token/refresh/` - Refresh access token

### Food Data
- `GET /api/categories/` - List all categories
- `GET /api/food-types/` - List all food types (filterable by category)
- `GET /api/food-types/:id/` - Get specific food type with ingredients
- `GET /api/ingredients/` - List all ingredients (filterable by food_type)

### Orders
- `POST /api/orders/` - Create a new order (authenticated or guest)
- `GET /api/orders/` - List user's orders (requires authentication)

## Features

- ✨ Premium dark theme with glassmorphism effects
- 🎨 Smooth animations using Framer Motion
- 🖱️ Drag-and-drop ingredient selection
- 📱 Responsive design
- 🔐 User authentication with JWT tokens
- 👤 User registration and login
- 📦 Order history for authenticated users
- 🔄 Reorder previous meals
- 🛒 Complete order management
- 👨‍💼 Admin dashboard for content management
- 🎯 Guest checkout option

## Development Notes

- Production backend: `https://backend-alx-project-production.up.railway.app/`
- Local backend (development): port 8000
- Frontend (development): port 3000
- CORS is enabled for development
- Media files are stored in production environment
- PostgreSQL is used in production; SQLite for local fallback

## Local PostgreSQL Setup (Windows)

1. Install PostgreSQL: Download from https://www.postgresql.org/download/ and complete installer (ensure pgAdmin and command line tools selected).
2. Create a database (after install, open Command Prompt):
```cmd
"%ProgramFiles%\PostgreSQL\16\bin\psql" -U postgres -c "CREATE DATABASE custom_food_builder;"
```
3. (Optional) Create a dedicated user:
```cmd
"%ProgramFiles%\PostgreSQL\16\bin\psql" -U postgres -c "CREATE USER cfb_user WITH PASSWORD 'cfb_pass';"
"%ProgramFiles%\PostgreSQL\16\bin\psql" -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE custom_food_builder TO cfb_user;"
```
4. Set environment variables in the same CMD session before running Django (temporary):
```cmd
set DB_ENGINE=postgresql
set POSTGRES_DB=custom_food_builder
set POSTGRES_USER=postgres
set POSTGRES_PASSWORD=postgres
set POSTGRES_HOST=localhost
set POSTGRES_PORT=5432
```
    For a custom user:
```cmd
set POSTGRES_USER=cfb_user
set POSTGRES_PASSWORD=cfb_pass
```
5. (Optional) Persist variables system-wide using `setx` (requires reopening terminals):
```cmd
setx POSTGRES_DB custom_food_builder
setx POSTGRES_USER postgres
setx POSTGRES_PASSWORD postgres
setx POSTGRES_HOST localhost
setx POSTGRES_PORT 5432
setx DB_ENGINE postgresql
```
6. Run migrations against PostgreSQL:
```cmd
python manage.py migrate
```
7. If you need to fall back to SQLite, either unset `DB_ENGINE` or set:
```cmd
set DB_ENGINE=sqlite
```

## Future Enhancements

- User authentication
- Order tracking
- Payment integration
- Multiple items per order
- Order history
- Image optimization