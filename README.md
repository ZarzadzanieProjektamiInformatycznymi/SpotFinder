SpotFinder
SpotFinder is a Django-based web platform designed for discovering and sharing interesting locations. Users can explore spots added by the community, contribute their own discoveries, and interact through ratings and comments.

🌟 Features
User Authentication: Secure registration and login system.

Spot Management: Users can add new locations with descriptions, categories, geolocation coordinates (Lat/Lng), and images.

Search & Filter: Find spots by name/description or filter them by specific categories.

Rating System: Users can rate spots on a scale of 1 to 5.

Comments: A discussion section for every spot to share tips and feedback.

Permissions: Only the creator of a spot can edit or delete it.

Responsive Design: Built with Bootstrap 5 for mobile and desktop compatibility.

🛠 Tech Stack
Python 3.x

Django (Web Framework)

SQLite (Default Database)

Bootstrap 5 (Frontend Styling)

🚀 Getting Started
Follow these instructions to set up the project locally on your machine.

Prerequisites
Ensure you have Python and pip installed on your system.

Installation
Clone the repository (or navigate to the folder):

cd SpotFinder
Create and activate a virtual environment:

Windows (PowerShell / VS Code):

python -m venv venv
.\venv\Scripts\Activate.ps1
macOS / Linux:

python3 -m venv venv
source venv/bin/activate
Install Dependencies:

pip install django pillow
(Or pip install -r requirements.txt if available)

Database Setup:

Apply the migrations to set up the database schema.

python manage.py makemigrations
python manage.py migrate
Load Sample Data (Optional):

To quickly populate the database with test categories, users (e.g., ania_podrozniczka, urban_explorer), and sample spots, run the provided script. This script cleans up old test data before adding new entries.

python load_sample_data.py
Create an Administrator:

To access the Django Admin panel:

python manage.py createsuperuser
▶️ Running the Application
Start the development server:

python manage.py runserver
Access the application:

Open your web browser and go to:

Homepage: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

📂 Project Structure Overview
models.py: Defines database structures for Spot, Category, Rating, Comment, and UserProfile.

views.py: Handles logic for listing spots, searching, CRUD operations, and processing user interactions.

forms.py: Custom forms for validating user input.

load_sample_data.py: Script to seed the database with initial data for testing.

templates/: HTML files utilizing the Django Template Language and Bootstrap 5.

🤝 Contributing
Fork the repository.

Create your feature branch (git checkout -b feature/NewFeature).

Commit your changes (git commit -m 'Add some NewFeature').

Push to the branch (git push origin feature/NewFeature).

Open a Pull Request.