# 🌺 Plant Care Tracker

A specialized Django web application designed to help enthusiasts manage their urban garden by tracking plant
collections and maintenance activities with a focus on timely care.

---

## 🌐 Live Application

The project is successfully deployed and can be accessed at:
🔗 **[Plant Care Tracker on Azure](https://plantcaretracker-g0bsfwfne3aaanaq.switzerlandnorth-01.azurewebsites.net/)**

---

## Project Overview

The **Plant Care Tracker** is an intuitive tool for logging plant data and care history. It solves the challenge of
remembering specific care schedules for different species by providing a centralized dashboard and a smart health
monitoring system.

---

### Key Features

* **Role-Based Access Control (RBAC):** Custom User model with two automated groups: **Gardeners** (Owners) and **Moderators**.
* **Asynchronous Task Processing:** Uses `asyncio` for background operations (e.g., clearing notifications alerts after adding care
  tasks) without blocking the main request-response cycle.
* **RESTful API:** Full API integration for plants and maintenance records with specialized serializers and object-level
  permissions.
* **Smart Health Monitoring:** Custom logic to identify "thirsty" plants based on watering frequency.
* **Cloud Storage:** Integrated with **Cloudinary** for professional media management in production.
* **Robust Testing:** Over **60 automated tests** covering models, views, forms, and API endpoints.

---

## Project Structure

The application is built using a modular architecture with six distinct Django apps:

* **`accounts`**: Custom User model and authentication logic.
* **`gardeners`**: Profile management and gardener-specific data.
* **`plants`**: Core plant management and tagging system.
* **`maintenance`**: Detailed care logs (Watering, Fertilizing, Pruning, Repotting).
* **`notifications`**: System alerts and automated reminders.
* **`common`**: Landing pages, global statistics, and error handling.

---

## Technical Implementation Highlights

* **Custom Template Tags:** Advanced logic implemented in `garden_extras.py` to calculate health scores dynamically.
* **Robust Validations:** Custom validators ensure data integrity (e.g., maintenance dates cannot precede a plant's
  creation date).
* **OOP Principles:** Applied throughout the views and models to ensure clean, maintainable, and reusable code.
* **Mixins:** Used to streamline logic and enforce consistency across multiple views.
* **Async Tasks**: The project uses `asyncio` for background processing. Check server logs during plant care updates to
  see async tasks executing seamlessly.
* **API Endpoints**: Accessible via `/api/plants/`, `api/plants/<slug:slug>/`, `api/maintenance/` and `api/maintenance/<int:pk>/`. Implements `IsAuthenticated` and ownership-based `ReadOnly`
  permissions.
* **Email Configuration**: Uses console.EmailBackend. Emails are displayed in the terminal.
* **Deployment**: Fully configured for **Azure App Service** with Gunicorn and WhiteNoise.

---

## Setup and Installation

### Prerequisites

* **Django 5.x**
* **Python 3.10+**
* **PostgreSQL**

### Installation Steps

1. **Clone the repository:**
   ```bash
    git clone https://github.com/SiyanaTrend/Plant-Care-Tracker.git
    cd Plant-Care-Tracker

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Environment Configuration**: Create a **`.env`** file in the root directory based on **`.env.example`**.
    * **Generate your SECRET_KEY**: Run the following command in your terminal to generate a secure key:
    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
    * **Set up your local PostgreSQL database and Email Configuration** and enter the credentials in the `.env` file.
    ```env
    SECRET_KEY=your_secret_key_here
    DEBUG=True    
    ALLOWED_HOSTS=localhost,127.0.0.1
    CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1

    DB_NAME=your_database_name
    DB_USER=your_postgres_user
    DB_PASSWORD=your_postgres_password
    DB_HOST=127.0.0.1
    DB_PORT=5432

    EMAIL_HOST_USER=your_email_host_user_here
    EMAIL_HOST_PASS=your_email_host_password_here
    COMPANY_EMAIL=your_verified_email@example.com

5. **Apply Migrations:**
    ```bash
    python manage.py migrate

6. **Run the Server:**
    ```bash
    python manage.py runserver

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   
8. **Testing**
    ```bash
    python manage.py test

---

## Data Management & Migrations

* **Initial Tags**: The project includes a **Data Migrations** that automatically prepopulates the database with
  essential tags (e.g., Indoor, Outdoor, Low Light) and creates 'Gardeners' and 'Moderators' groups with
  pre-defined permissions upon migration upon the first migration.
* **Tag Moderation System**: To ensure data quality, users can suggest new tags, but these remain "pending" (hidden) by
  default.
* **Approval Workflow**: Tags feature an `is_approved` field. Only users with **Moderator** or **Superuser** status can
  approve and manage these tags through the **Django Admin Panel**, making them visible to the public.
* **Integrity**: The **`Tag`** model includes normalization logic and unique constraints to prevent duplicate entries
  and ensure consistent naming across the platform.

---

## Evaluation Notes

* **Navigation**: All pages are connected via a consistent navigation bar and footer.
* **Database**: The project is configured specifically for **PostgreSQL**.Users must ensure a local DB instance is
  running before applying migrations.

---

## Credentials for Testing
* **Superuser**: To manage the project, create a local superuser using `python manage.py createsuperuser`.
* **Moderator Access**: Assign a user to the **Moderators** group and set `is_staff=True` in the Admin panel to test the tag approval workflow.

