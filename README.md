# Django Movies API

A simple REST API built with Django and Django REST Framework for managing a movie database. This project demonstrates CRUD operations with PostgreSQL integration.

## 🎬 Features

- **Movie Management**: Create, read, update, and delete movies
- **REST API**: RESTful endpoints for movie data
- **PostgreSQL Database**: Robust database backend
- **Django Admin**: Web-based admin interface for data management
- **Environment Configuration**: Secure configuration with environment variables

## 🛠️ Tech Stack

- **Backend**: Django 5.2.7
- **API Framework**: Django REST Framework
- **Database**: PostgreSQL
- **Environment Management**: python-decouple
- **Language**: Python

## 📋 Movie Model

The API manages movies with the following attributes:
- `title` - Movie title (max 200 characters)
- `director` - Director name (max 100 characters) 
- `release_year` - Year of release (positive integer)
- `genre` - Movie genre (max 50 characters)

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and navigation info |
| GET | `/movies/` | List all movies |
| GET | `/admin/` | Django admin interface |

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/hadhiabdulla/django-movies-project.git
cd django-movies-project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django djangorestframework psycopg2-binary python-decouple
```

### 4. Database Setup
1. Create a PostgreSQL database named `movies_db`
2. Update the `.env` file with your database credentials:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=movies_db
DB_USER=your-db-username
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Start Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📖 Usage Examples

### Get All Movies
```bash
curl -X GET http://localhost:8000/movies/
```

### Access Admin Panel
Navigate to `http://localhost:8000/admin/` and log in with your superuser credentials.

## 📁 Project Structure
```
django-movies-project/
├── movies/                 # Main app directory
│   ├── __init__.py
│   ├── models.py          # Movie model definition
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # App URL patterns
│   ├── admin.py           # Admin configuration
│   └── apps.py            # App configuration
├── movies_project/         # Project configuration
│   ├── __init__.py
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── .env                   # Environment variables
├── manage.py              # Django management script
└── README.md              # Project documentation
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=movies_db
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Hadhi Abdulla**
- GitHub: [@hadhiabdulla](https://github.com/hadhiabdulla)

## 🙏 Acknowledgments

- Django and Django REST Framework documentation
- PostgreSQL community
- Open source community
