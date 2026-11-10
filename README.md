# Little Lemon Restaurant API

## Project Description

This project is the backend API for the Little Lemon restaurant, developed as part of the Meta Back-End Developer Capstone project on Coursera.

The API provides functionality for managing restaurant menu items and table bookings. It uses Django REST Framework to build RESTful endpoints and MySQL as the database.

## Technologies Used

- Python 3.13
- Django 5.2
- Django REST Framework
- MySQL 8.4
- Djoser
- Django REST Framework Token Authentication
- Insomnia (API testing)

## Project Features

- User registration and authentication.
- Token-based authentication.
- Menu item management (CRUD).
- Table booking management (CRUD).
- MySQL database integration.
- Django Admin interface.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/felfeit/coursera-meta-backend-dev-capstone.git
cd coursera-meta-backend-dev-capstone
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory using `.env.example` as a reference.

Configure the following variables:

```env
DB_NAME=LittleLemon
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

Make sure MySQL is running and the database exists before continuing.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

### Authentication

| Method | Endpoint              | Description                 |
| ------ | --------------------- | --------------------------- |
| POST   | `/auth/users/`        | Register a new user         |
| GET    | `/auth/users/me/`     | Retrieve current user       |
| POST   | `/auth/token/login/`  | Obtain authentication token |
| POST   | `/auth/token/logout/` | Log out                     |

### Menu

| Method | Endpoint                 | Description                  |
| ------ | ------------------------ | ---------------------------- |
| GET    | `/restaurant/menu/`      | Retrieve all menu items      |
| POST   | `/restaurant/menu/`      | Create a menu item           |
| GET    | `/restaurant/menu/<id>/` | Retrieve a menu item         |
| PUT    | `/restaurant/menu/<id>/` | Update a menu item           |
| PATCH  | `/restaurant/menu/<id>/` | Partially update a menu item |
| DELETE | `/restaurant/menu/<id>/` | Delete a menu item           |

### Table Booking

| Method | Endpoint                           | Description                |
| ------ | ---------------------------------- | -------------------------- |
| GET    | `/restaurant/booking/tables/`      | Retrieve all bookings      |
| POST   | `/restaurant/booking/tables/`      | Create a booking           |
| GET    | `/restaurant/booking/tables/<id>/` | Retrieve a booking         |
| PUT    | `/restaurant/booking/tables/<id>/` | Update a booking           |
| PATCH  | `/restaurant/booking/tables/<id>/` | Partially update a booking |
| DELETE | `/restaurant/booking/tables/<id>/` | Delete a booking           |

**Note:** Table booking endpoints require token authentication.

To authenticate, include the following HTTP header:

```http
Authorization: Token your_auth_token
```

## Running Tests

Run the automated test suite with:

```bash
python manage.py test
```

Check the Django project configuration with:

```bash
python manage.py check
```

## Admin Interface

Access the Django administration panel at:

`http://127.0.0.1:8000/admin/`

Create a superuser with:

```bash
python manage.py createsuperuser
```

## License

This project was developed for educational purposes as part of the Meta Back-End Developer Capstone project on Coursera.