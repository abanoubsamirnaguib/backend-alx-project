# 🛒 Food Ordering E-Commerce Platform - ALX ProDev Backend Project

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=railway&logoColor=white)

A comprehensive **e-commerce food ordering platform** built as part of the **ALX ProDev Backend Engineering Program**. This application demonstrates modern e-commerce architecture with advanced features including product catalog management,order processing, and customer management systems.

## 🚀 Live Demo

**🌐 Production Deployment**: [https://backend-alx-project-production.up.railway.app/](https://backend-alx-project-production.up.railway.app/)

**🖥️ Frontend Application**: [https://frontend-alx-project-2.vercel.app/menu](https://frontend-alx-project-2.vercel.app/menu)

**📚 API Documentation**: [https://backend-alx-project-production.up.railway.app/api/](https://backend-alx-project-production.up.railway.app/api/)

**⚙️ Admin Panel**: [https://backend-alx-project-production.up.railway.app/admin/login/?next=/admin/](https://backend-alx-project-production.up.railway.app/admin/login/?next=/admin/)

### Demo Credentials For Admin Panel
```
Username: admin
Password: 12345678
```

## 🎯 E-Commerce Platform Overview

This food ordering e-commerce platform provides a complete online marketplace solution featuring:
- 🛍️ **Product Catalog Management** - Categories, food types, and ingredient inventory
- 🛒 **Shopping Cart System** - Add, customize, and manage cart items
- 💳 **Order Processing** - Complete checkout flow with customer details
- 👥 **Customer Management** - User accounts, profiles, and order history
- 📱 **Guest Checkout** - Allow purchases without registration
- 📊 **Order Fulfillment** - Order tracking and management system
- 🏪 **Admin Commerce Dashboard** - Product, order, and customer management
- 💰 **Pricing Engine** - Dynamic pricing with base costs and add-on ingredients

## 🏗️ Architecture & Tech Stack

### Backend Technologies
- **Python 3.11+** - Core programming language
- **Django 5.0** - High-level web framework
- **Django REST Framework** - Powerful API development toolkit
- **PostgreSQL** - Production database (SQLite for development)
- **JWT Authentication** - Secure token-based authentication
- **Pillow** - Image processing and handling
- **Gunicorn** - WSGI HTTP Server for production
- **WhiteNoise** - Static file serving

### Infrastructure & Deployment
- **Railway** - Cloud platform for deployment
- **Docker** - Containerization (production-ready)
- **CI/CD Pipeline** - Automated deployment workflows
- **Vercel** - Frontend deployment and hosting platform

### Development Tools
- **python-dotenv** - Environment variable management
- **django-cors-headers** - Cross-origin resource sharing
- **django-filter** - Advanced filtering capabilities

## 📁 Project Structure

```
backend/
├── 📁 config/                    # Django project configuration
│   ├── __init__.py
│   ├── settings.py               # Main settings with environment configs
│   ├── urls.py                   # Root URL configuration
│   ├── asgi.py                   # ASGI configuration for async
│   └── wsgi.py                   # WSGI configuration for deployment
│
├── 📁 api/                       # Core API application
│   ├── __init__.py
│   ├── models.py                 # Database models & relationships
│   ├── serializers.py            # DRF serializers for data validation
│   ├── views.py                  # API endpoints & business logic
│   ├── urls.py                   # API routing configuration
│   ├── admin.py                  # Django admin customization
│   ├── apps.py                   # App configuration
│   └── 📁 management/            # Custom Django commands
│       └── 📁 commands/
│           ├── createsuperuser_auto.py  # Automated superuser creation
│           └── seed_data.py             # Database seeding
│
├── 📁 media/                     # User-uploaded files
│   ├── 📁 categories/            # Category images
│   ├── 📁 food_types/            # Food type images
│   └── 📁 ingredients/           # Ingredient images
│
├── 📁 staticfiles/               # Collected static files for production
│
├── 🐳 Dockerfile                 # Docker container configuration
├── 📋 requirements.txt           # Python dependencies
├── ⚙️ manage.py                  # Django management script
├── 🗄️ db.sqlite3               # SQLite database (development)
├── 🚀 deploy_railway.sh         # Railway deployment script
├── 📝 railway.toml              # Railway configuration
└── 📜 Procfile                  # Process configuration for Railway
```

## 🗄️ E-Commerce Database Schema

### Product Catalog & Order Management Models

```python
# Product Category Model (E-Commerce Catalog)
Category
├── id (Primary Key)
├── name (CharField)          # Category name (e.g., "Burgers", "Desserts")
└── image (ImageField)        # Category display image

# Product Model (Food Items)
FoodType
├── id (Primary Key)
├── category (ForeignKey → Category)  # Product categorization
├── name (CharField)                  # Product name
├── base_price (DecimalField)         # Base product price
└── image (ImageField)                # Product display image

# Product Add-ons/Variants Model
Ingredient
├── id (Primary Key) 
├── food_type (ForeignKey → FoodType) # Product relationship
├── name (CharField)                  # Add-on name (e.g., "Extra Cheese")
├── price (DecimalField)              # Additional cost for add-on
├── image (ImageField)                # Add-on visual representation
├── layer_order (IntegerField)        # Display order for customization
└── is_default (BooleanField)         # Included in base price

# Customer Order Model (E-Commerce Transaction)
Order
├── id (Primary Key)
├── user (ForeignKey → User, nullable)  # Registered customer
├── is_guest (BooleanField)             # Guest checkout support
├── customer_name (CharField)           # Billing/shipping name
├── phone_number (CharField)            # Contact information
├── address (TextField)                 # Delivery address
├── notes (TextField)                   # Special instructions
├── created_at (DateTimeField)          # Order timestamp
└── total_price (DecimalField)          # Final order total

# Shopping Cart/Order Line Items
OrderItem
├── id (Primary Key)
├── order (ForeignKey → Order)               # Order relationship
├── food_type (ForeignKey → FoodType)        # Base product
├── selected_ingredients (ManyToManyField)   # Selected add-ons
└── ingredients_order (JSONField)            # Customization sequence
```

## 🚀 API Documentation

*This API powers the frontend application deployed on **Vercel** at [https://frontend-alx-project-2.vercel.app/](https://frontend-alx-project-2.vercel.app/)*

### Base URL
```
Production: https://backend-alx-project-production.up.railway.app/api/
Local:      http://localhost:8000/api/
```

### 🔐 Authentication Endpoints

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "string",
  "email": "string", 
  "password": "string",
  "first_name": "string",
  "last_name": "string"
}
```

**Response (201):**
```json
{
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "refresh": "jwt_refresh_token",
  "access": "jwt_access_token"
}
```

#### Login User
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "string",
  "password": "string"
}
```

#### User Profile
```http
GET /api/auth/profile/
Authorization: Bearer <access_token>
```

#### Refresh Token
```http
POST /api/auth/token/refresh/
Content-Type: application/json

{
  "refresh": "jwt_refresh_token"
}
```

### 🛍️ E-Commerce Catalog Endpoints

#### Get All Categories
```http
GET /api/categories/
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Burgers",
    "image": "/media/categories/burgers.jpg",
    "food_types": [
      {
        "id": 1,
        "name": "Classic Burger",
        "base_price": "8.99",
        "image": "/media/food_types/classic_burger.jpg"
      }
    ]
  }
]
```

#### Get Food Types
```http
GET /api/food-types/
GET /api/food-types/?category=1  # Filter by category
```

#### Get Food Type Details
```http
GET /api/food-types/1/
```

**Response:**
```json
{
  "id": 1,
  "category": 1,
  "name": "Classic Burger",
  "base_price": "8.99",
  "image": "/media/food_types/classic_burger.jpg",
  "ingredients": [
    {
      "id": 1,
      "name": "Beef Patty",
      "price": "0.00",
      "image": "/media/ingredients/beef_patty.jpg",
      "layer_order": 1,
      "is_default": true
    },
    {
      "id": 2,
      "name": "Cheese",
      "price": "1.50",
      "image": "/media/ingredients/cheese.jpg", 
      "layer_order": 2,
      "is_default": false
    }
  ]
}
```

#### Get Ingredients
```http
GET /api/ingredients/
GET /api/ingredients/?food_type=1  # Filter by food type
```

### 🛒 E-Commerce Order Processing

#### Create Order
```http
POST /api/orders/
Content-Type: application/json

{
  "is_guest": false,
  "customer_name": "John Doe",
  "phone_number": "+1234567890",
  "address": "123 Main St, City, State",
  "notes": "Extra crispy fries",
  "items": [
    {
      "food_type": 1,
      "selected_ingredients": [1, 2, 3],
      "ingredients_order": [1, 2, 3]
    }
  ]
}
```

#### Get User Orders (Authenticated)
```http
GET /api/orders/
Authorization: Bearer <access_token>
```

### 🏥 System Health
```http
GET /api/health/
```

**Response:**
```json
{
  "status": "healthy",
  "django_version": "5.0.0",
  "database": "connected",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## 🎓 ALX ProDev Backend Engineering - Learning Journey

### Program Overview
This project represents the culmination of the **ALX ProDev Backend Engineering Program**, a comprehensive 6-month intensive that covers modern backend development practices, cloud technologies, and software engineering principles.

### 🔧 Key Technologies Mastered

#### **Python & Django Ecosystem**
- **Django Framework**: Built robust web applications using Django's MVT architecture
- **Django REST Framework**: Developed RESTful APIs with advanced serialization and viewsets
- **Django Admin**: Customized admin interfaces for content management
- **Django ORM**: Implemented complex database relationships and queries

#### **API Development & Documentation**
- **RESTful Design**: Applied REST principles for scalable API architecture
- **JWT Authentication**: Implemented secure token-based authentication
- **API Serialization**: Data validation and transformation using DRF serializers
- **Cross-Origin Resource Sharing**: Configured CORS for frontend integration

#### **Database Design & Management**
- **PostgreSQL**: Production database with advanced features
- **SQLite**: Development database for rapid prototyping
- **Database Migrations**: Version control for database schema changes
- **Model Relationships**: One-to-Many, Many-to-Many, Foreign Keys

#### **Cloud Infrastructure & DevOps**
- **Railway Deployment**: Cloud platform deployment with CI/CD
- **Docker Containerization**: Created production-ready containers
- **Environment Management**: Configuration for multiple environments
- **Static File Handling**: WhiteNoise for efficient static file serving

### 💡 Important Backend Concepts Learned

#### **E-Commerce Database Design**
- **Product Catalog Architecture**: Hierarchical category-product-variant structure
- **Order Management System**: Complete order lifecycle from cart to fulfillment
- **Customer Data Management**: User profiles, guest checkout, and order history
- **Inventory Relationships**: Product-ingredient many-to-many with pricing logic
- **Normalized E-Commerce Schema**: Eliminated data redundancy across commerce entities
- **Query Optimization**: Efficient product and order queries with relationship loading

#### **API Architecture & Security**
- **Token-Based Authentication**: JWT implementation for stateless authentication
- **Permission Classes**: Role-based access control
- **Data Validation**: Input sanitization and validation layers
- **Error Handling**: Comprehensive error responses and logging

#### **Asynchronous Programming**
- **ASGI Configuration**: Prepared for async view handling
- **Background Tasks**: Understanding of task queues and workers
- **Real-time Features**: WebSocket preparation for live updates

#### **Caching Strategies**
- **Django Caching Framework**: Implementation ready for Redis/Memcached
- **Database Query Optimization**: Reduced database hits through efficient queries
- **Static File Caching**: CDN-ready static file configuration

### 🏆 Challenges Overcome & Solutions

#### **Challenge 1: E-Commerce Product Customization**
**Problem**: Managing complex product variants where customers can customize food items with multiple add-ons while maintaining accurate pricing and order tracking.

**Solution**: Implemented a flexible product-variant system using many-to-many relationships with JSONField for custom ordering, enabling dynamic pricing calculation and order accuracy.

```python
# E-Commerce product customization solution
class OrderItem(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)  # Base product
    selected_ingredients = models.ManyToManyField(Ingredient)         # Customer add-ons
    ingredients_order = models.JSONField(default=list, blank=True)    # Custom sequence
```

#### **Challenge 2: Image Upload & Media Handling**
**Problem**: Handling user-uploaded images efficiently in both development and production environments.

**Solution**: Implemented proper media file handling with Django's ImageField and configured static file serving for production.

#### **Challenge 3: E-Commerce Customer Experience**
**Problem**: Supporting both registered customers (with order history and profiles) and guest checkout to maximize conversion rates.

**Solution**: Designed flexible customer management system that handles both user types while maintaining order tracking capabilities:

```python
def get_queryset(self):
    if self.request.user.is_authenticated:
        return Order.objects.filter(user=self.request.user).order_by('-created_at')
    return Order.objects.none()
```

#### **Challenge 4: Production Deployment Configuration**
**Problem**: Managing different configurations for development and production environments.

**Solution**: Environment-based configuration management with proper secret handling and database switching.

### 🎯 Best Practices Implemented

#### **Code Organization**
- **Separation of Concerns**: Clear distinction between models, views, serializers
- **DRY Principle**: Reusable components and minimal code duplication
- **Custom Management Commands**: Automated setup and data seeding
- **Proper Import Structure**: Organized imports and dependencies

#### **Security Implementation**
- **Environment Variables**: Sensitive data protection
- **CORS Configuration**: Secure cross-origin resource sharing
- **Input Validation**: Multiple layers of data validation
- **Token Security**: Proper JWT implementation with refresh mechanisms

#### **Performance Optimization**
- **Database Query Optimization**: Efficient ORM usage
- **Static File Management**: Production-ready static file handling
- **Media File Organization**: Structured file upload system
- **Caching Ready**: Prepared for production caching implementation

### 🚀 Personal Growth & Key Takeaways

#### **Technical Skills Developed**
1. **Full-Stack Understanding**: Deep comprehension of backend-frontend integration
2. **DevOps Fundamentals**: Hands-on experience with cloud deployment
3. **Database Expertise**: Advanced relational database design and optimization
4. **API Design**: RESTful API development with industry standards

#### **Professional Development**
1. **Problem-Solving**: Systematic approach to debugging and optimization
2. **Documentation Skills**: Comprehensive API documentation and code comments
3. **Version Control**: Git workflow for collaborative development
4. **Testing Mindset**: Understanding of testing strategies and quality assurance

#### **Industry-Ready Skills**
- **Scalable Architecture**: Designed for horizontal scaling
- **Production Deployment**: Real-world deployment experience
- **Security-First Approach**: Implementation of security best practices
- **Performance Awareness**: Built with optimization in mind


## 🚀 Local Development Setup

### Prerequisites
- Python 3.11+
- PostgreSQL (for production-like setup)
- Git

### Installation Steps

1. **Clone the repository:**
```cmd
git clone <repository-url>
cd backend
```

2. **Create virtual environment:**
```cmd
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```cmd
pip install -r requirements.txt
```

4. **Environment configuration:**
Create `.env` file in root directory:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. **Run migrations:**
```cmd
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser:**
```cmd
python manage.py createsuperuser
```

7. **Load sample data:**
```cmd
python manage.py seed_data
```

8. **Start development server:**
```cmd
python manage.py runserver
```

Visit: `http://localhost:8000/api/` for API and `http://localhost:8000/admin/` for admin panel.

## 📄 License

This project is part of the ALX ProDev Backend Engineering Program and is for educational purposes.

---

**Built with ❤️ as part of the ALX ProDev Backend Engineering Program**

*Demonstrating advanced backend development concepts, cloud deployment strategies, and modern software engineering practices.*
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