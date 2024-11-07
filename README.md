# RecipeVerse - Recipe Management System 

RecipeVerse is a web application built with Django that allows users to create, manage, and share their favorite recipes. Users can add detailed recipes with ingredients, instructions, and images.

## Features

- User Authentication System
  - Register new account
  - Login/Logout functionality
  - Password management
  - User-specific recipe management

- Recipe Management
  - Create new recipes with title, ingredients, instructions, and images
  - View detailed recipe information
  - Edit existing recipes
  - Delete recipes
  - Image upload functionality
  - Ingredients list with line-by-line entry

- User Interface
  - Responsive design
  - Grid layout for recipe display
  - Detailed view for each recipe
  - User-friendly forms for recipe creation and editing
  - Mobile-friendly layout


## Technology Stack

- Backend: Django 5.1.2
- Database: SQLite/PostgreSQL
- Frontend: HTML, CSS
- Image Processing: Pillow 11.0.0
- Python: 3.x
- Additional Dependencies: Listed in requirements.txt

## Installation

1. Clone the repository
```bash
git clone https://github.com/adit-syntax/recipe-app
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Apply database migrations
```bash
python manage.py migrate
```

5. Create a superuser (Admin)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

7. Access the application at `http://localhost:8000`


## Project Structure

```
recipe_project/
├── accounts/              # User authentication app
├── media/                 # Uploaded media files
├── recipe_app/           # Main recipe application
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/               # Static files (CSS, JS)
│   └── css/
│       └── style.css
├── templates/            # HTML templates
│   ├── recipe_app/
│   └── registration/
├── manage.py
└── requirements.txt
```
