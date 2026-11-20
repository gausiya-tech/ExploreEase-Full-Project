# ExploreEase – Tour & Travel Website

A Django-based full-stack starter project based on the supplied Tour & Travel Website presentation. It combines the Django backend, database models, forms, admin panel, templates and responsive CSS/JavaScript frontend.

## Included modules
- Home page and navigation
- Tour packages and package details
- Booking request form
- Contact Us form
- Travel gallery
- Reviews submission and display
- About Us and team display
- Django Admin for City, Package, Booking, Contact, Gallery, Review, Team and Feedback records

## Requirements
- Python 3.10+
- pip

## Windows setup (PowerShell)
1. Extract this ZIP.
2. Open PowerShell inside the `ExploreEase_Backend` folder (the folder containing `manage.py`).
3. Create and activate a virtual environment:
   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
4. Install packages:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Create database tables:
   ```powershell
   python manage.py makemigrations tours
   python manage.py migrate
   ```
6. Create an admin account:
   ```powershell
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```powershell
   python manage.py runserver
   ```
8. Open `http://127.0.0.1:8000/` for the website and `http://127.0.0.1:8000/admin/` for the admin panel.

## Add website content
Log in to the admin panel and add Cities first, then Packages. Add Gallery photos and Team members there too. The public pages display records added through the admin.

## Notes
- SQLite is configured by default; it is suitable for local development and demos.
- This is a learning/demo starter, not a deployed production site. Configure a production secret key, `DEBUG=False`, allowed hosts, static/media hosting and HTTPS before deployment.
- Online payments, real-time hotel/transport availability, and automated email/SMS notifications are future-scope features and are not implemented in this starter.
- The supplied presentation names modules and data fields; this starter implements those core records and pages. Review the code with your team and adapt it to your institute's exact requirements.
