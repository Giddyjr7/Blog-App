# Blog App

A Flask-based blogging application that allows users to create, edit, and manage blog posts with authentication features.

## Features

- User Authentication (Sign Up, Login, Logout)
- Create, Edit, and Delete Blog Posts
- Comment System
- Category Management
- Responsive Design

## Technologies Used

- Python/Flask
- SQLite Database
- Flask-SQLAlchemy
- Flask-Login for authentication
- HTML/CSS
- Bootstrap for styling

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Giddyjr7/Blog-App.git
cd Blog-App
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python3 app.py
```

4. Access the application at `http://127.0.0.1:5000`

## Project Structure

- `/website` - Main application package
  - `/templates` - HTML templates
  - `/static` - CSS, JavaScript, and images
  - `models.py` - Database models
  - `views.py` - Route handlers
  - `auth.py` - Authentication logic

## Database

The application uses SQLite as the database, with the following main tables:
- Users
- Posts
- Comments
- Categories

## License

MIT License
