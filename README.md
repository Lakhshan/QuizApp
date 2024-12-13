# Django Quiz App

A simple quiz application built using Django. This app allows a user to take a quiz, answer random multiple-choice questions, and view the results with details about correct and incorrect submissions.

Features
Start a new quiz session.
Get a random multiple-choice question.
Submit an answer for each question.
View the summary of the total questions answered, along with correct and incorrect answers.

## Prerequisites
- Python 3.8+ (for development)
- Django 4.0+ (for the web framework)

## Installation
**1. Clone the Repository**
````
git clone https://github.com/yourusername/django-quiz-app.git
cd django-quiz-app
````
**2. Create a Virtual Environment (optional but recommended)**
```
python -m venv venv
```
Activate the virtual environment:

On Windows:

```
venv\Scripts\activate
```
On macOS/Linux:

```
source venv/bin/activate
```
**3. Install Dependencies**
```
pip install -r requirements.txt
```
If you don't have the requirements.txt file, you can generate it by running:
```
pip freeze > requirements.txt
```
**4. Apply Migrations**

Make sure to apply the database migrations to set up your models:
```
python manage.py migrate
```
**5. Create a Superuser (Optional)**

To access the Django admin panel and add quiz questions, create a superuser:
```
python manage.py createsuperuser
```
**6. Run the Development Server**

Start the Django development server to access the quiz app:

```
python manage.py runserver
```
Visit the app in your browser at http://127.0.0.1:8000/ to start the quiz!
