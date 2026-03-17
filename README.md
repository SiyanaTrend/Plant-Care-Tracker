# 🌺 Plant Care Tracker

A specialized Django web application designed to help enthusiasts manage their urban garden by tracking plant
collections and maintenance activities with a focus on timely care.

---

## Project Overview

The **Plant Care Tracker** is an intuitive tool for logging plant data and care history. It solves the challenge of
remembering specific care schedules for different species by providing a centralized dashboard and a smart health
monitoring system.

### Key Features

* **Full CRUD Management:** Complete control over Plants, Gardeners, and Maintenance records.
* **Smart Garden Health Algorithm:** A custom-built logic that identifies "thirsty" plants by comparing their specific
  watering frequency against the date of their last recorded care.
* **Maintenance History:** Detailed logs of every action taken (Watering, Fertilizing, Pruning) with notes.
* **Statistics Dashboard:** Real-time analytics showcasing overall garden health, "Star Plants" (most cared for), and
  popular categories.
* **Custom User Experience:** Includes a custom 404 error page and interactive UI elements for easy navigation.

---

## Project Structure

The application is built using a modular architecture with four distinct Django apps:

* **`common`**: Manages the landing page (Home) and the complex Statistics dashboard.
* **`gardener`**: Handles full CRUD operations for the gardener's profile.
* **`plants`**: The core app for plant management, including the tagging system.
* **`maintenance`**: Manages the care logs and historical records for each plant.

---

## Technical Implementation Highlights

* **Custom Template Tags:** Advanced logic implemented in `garden_extras.py` to calculate health scores dynamically.
* **Robust Validations:** Custom validators ensure data integrity (e.g., maintenance dates cannot precede a plant's
  creation date).
* **OOP Principles:** Applied throughout the views and models to ensure clean, maintainable, and reusable code.
* **Mixins:** Used to streamline logic and enforce consistency across multiple views.

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

3. **Install dependencies::**
   ```bash
   pip install -r requirements.txt

4. **Environment Configuration**: Create a **`.env`** file in the root directory based on **`.env.example`**.
    * **Generate your SECRET_KEY**: Run the following command in your terminal to generate a secure key:
      ```bash
      python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
      ```
    * **Set up your local PostgreSQL database** and enter the credentials in the `.env` file.
    ```env
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    
    DB_NAME=your_database_name
    DB_USER=your_postgres_user
    DB_PASSWORD=your_postgres_password
    DB_HOST=127.0.0.1
    DB_PORT=5432
5. **Apply Migrations:**
    ```bash
    python manage.py migrate

6. **Run the Server:**
    ```bash
    python manage.py runserver

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
---

## Data Management & Migrations

* **Initial Tags**: The project includes a **Data Migration** that automatically prepopulates the database with
  essential tags (e.g., Indoor, Outdoor, Low Light) upon the first migration.
* **Tag Management**: New tags can be managed exclusively through the **Django Admin Panel**.
* **Integrity**: The **`Tag`** model includes normalization logic and unique constraints to prevent duplicate entries
  and ensure consistent naming.

---

## Evaluation Notes

* **No Authentication**: As per requirements, the system does not use Django's auth module. All features are accessible
  for evaluation purposes.
* **Navigation**: All pages are connected via a consistent navigation bar and footer.
* **Database**: The project is configured specifically for **PostgreSQL**.Users must ensure a local DB instance is
  running before applying migrations.
