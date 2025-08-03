-------------------------------------------------Ride-Sharing-API-------------------------------------------------------------

A basic ride-sharing API built with Django and Django REST Framework. This application simulates a simple ride-sharing system with user roles (rider/driver), JWT-based authentication, and endpoints to request and accept rides.

---

Features

- Custom user model with roles: `rider` and `driver`
- JWT Authentication with `SimpleJWT`
- Riders can request rides
- Drivers can fetch available rides and accept them
- Real-time ride location simulation (Bonus Phase I)
- Modular, testable code structure

---

Tech Stack

- Python 3.10.12
- Django 5.2.4
- Django REST Framework 3.16.0
- djangorestframework-simplejwt 5.5.1
- SQLite (default)

---

Project Structure

ride-sharing-api/
├── accounts/ # User model app
│ ├── models.py # User model
│ ├── views.py # ViewSets and business logic
│ ├── serializers.py # DRF serializers
│ ├── urls.py # API routes
├── api/ # Core app
│ ├── models.py # Ride model
│ ├── views.py # ViewSets and business logic
│ ├── serializers.py # DRF serializers
│ ├── urls.py # API routes
├── ride_sharing/ # Project settings
├── manage.py


---

Setup Instructions

---

1. Clone the Repository

```bash
git clone https://github.com/yourusername/ride-sharing-api.git
cd ride-sharing-api

2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Run the Server

python manage.py runserver

---


Authentication
Uses JWT via djangorestframework-simplejwt

Endpoints:

POST /api/token/ – Get access and refresh tokens

POST /api/token/refresh/ – Refresh token


---

User Roles

POST /api/register/

{
  "username": "driver1",
  "email": "driver1@example.com",
  "password": "pass1234",
  "role": "driver"
}


---

API Endpoints

| Endpoint                       | Method | Role   | Description                           |
| ------------------------------ | ------ | ------ | ------------------------------------- |
| `/api/users/`                  | POST   | Public | Register as rider or driver           |
| `/api/token/`                  | POST   | Public | Get JWT token                         |
| `/api/rides/`                  | GET    | Driver | List available rides                  |
| `/api/rides/`                  | POST   | Rider  | Request a ride                        |
| `/api/rides/<id>/accept/`      | POST   | Driver | Accept a ride                         |
| `/api/rides/location/`         | POST   | Driver | Simulate live location update         |
| `/api/users/me/`               | GET    | Auth   | View current user info                |


# Author
Developed by Vishnu Chandran
[Your LinkedIn or GitHub Profile link if applicable]

# License
This project is licensed under the MIT License.


