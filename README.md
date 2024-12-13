# Django Quiz App 📝

A simple Django-based web application for a quiz system. This app allows a single user to:

- Start a new quiz session.
- Answer randomly selected multiple-choice questions.
- Submit answers and view results, including correct and incorrect submissions.

Features
- **Quiz Session Management:** Start a new quiz session.
- **Random Questions:** Fetch a random question from the database.
- **Answer Submission:** Submit answers and receive feedback.
- **Progress Tracking:** View statistics such as total questions answered and a breakdown of correct/incorrect answers.

## Usage
- Start a New Quiz: Click on "Start a New Quiz" to begin the session.
- Answer Questions: Select an option for each question and submit.
- View Summary: Once you've answered all questions, view the summary of correct and incorrect answers.

## Prerequisites
- Python 3.8+
- Django 4.0+
- SQLite (default database, or any other database supported by Django)

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
pip install dajango
```
**4. Apply Migrations**

   Make sure to apply the database migrations to set up your models:
```
python manage.py makemigrations
python manage.py migrate
```
**5. Create a Superuser (for managing questions via Django Admin)**

To access the Django admin panel and add quiz questions, create a superuser:
```
python manage.py createsuperuser
```
**6. Run the Development Server**

Start the Django development server to access the quiz app:

```
python manage.py runserver
```

**7.Access the Application:**
- Open your browser and navigate to http://127.0.0.1:8000/quiz/
- Access the admin panel at http://127.0.0.1:8000/admin/ to add questions.

## API Endpoints


**1. Start Quiz Session**

URL: `/quiz/start/`

Method: `GET`

Response:  `{ "message": "New quiz session started", "session_id": <id> }`


**2.Get Random Question**

URL: `/quiz/question/<session_id>/`

Method: `GET`

Response:
```
{
    "question_id": 1,
    "question_text": "What is the capital of India?",
    "options": {
        "A": "Delhi",
        "B": "Bangalore ",
        "C": "Mumbai",
        "D": "Madrid"
    }
}

```


**3.Submit Answer**

URL: `/quiz/submit/<session_id>/?question_id=<id>&selected_option=<option>`

Method: GET

Response: { "message": "Answer submitted" }



**4.Get Score**

URL: `/quiz/score/<session_id>/`

Method: `GET`

Response:
```
{
    "total_questions": 5,
    "correct_answers": 3,
    "incorrect_answers": 2
}
```

## Adding Questions
- Log in to the Django Admin panel at /admin/.
- Add new questions under the Questions model. Provide the question text, options, and the correct answer.

