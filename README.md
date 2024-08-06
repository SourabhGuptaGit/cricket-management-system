# **Cricket Management System**

## **Overview**

The **Cricket Management System** is a web-based application built using the Django framework. It is designed to efficiently manage and track cricket teams, players, match fixtures, and points tables. This application provides an intuitive interface for users to view details about teams, players, and match outcomes, making it ideal for sports organizations, cricket enthusiasts, or developers looking to explore Django.

## **Features**

- **Team Management**
  - View a list of cricket teams with their logos.
  - Click on a team to view detailed information, including the list of players and their statistics.

- **Player Management**
  - Display detailed information about individual players, including their image, jersey number, country, and performance statistics (e.g., matches played, runs scored, highest scores, fifties, hundreds).

- **Match Fixtures**
  - Generate random fixtures between teams.
  - Display match results, including the winner.

- **Points Table**
  - Track and display the points earned by teams based on match outcomes.
  - View a detailed points table, including matches played, matches won, matches lost, and total points.

## **Technical Stack**

- **Backend:** Django (Python)
- **Database:** PostgreSQL (configurable via environment variables)
- **Frontend:** HTML, CSS (with responsive design)
- **Environment Configuration:** Managed via a `.env` file for security and flexibility.
- **Deployment:** Production-ready setup with environment variable management and adherence to SOLID principles.

## Requirements

- Python 3.12
- Django 5.0.7
- python-dotenv 1.0.1 (for environment variables)
- sqlparse 0.5.1

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SourabhGuptaGit/cricket-management-system.git
cd cricket-management-system
```

### 2. Create and Activate a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a .env file in the root directory of the project with the following content:
```
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
ALLOWED_HOSTS=127.0.0.1, .localhost
```

### 5. Create a Superuser
Create a superuser to access the Django admin panel:

```
python manage.py createsuperuser
```

## Project Structure
Here's a brief overview of the project structure:

```
cricket-management-system/
│
├── cricket_management/      # Main Django project directory
│   ├── settings.py          # Django settings file (configured to use environment variables)
│   ├── urls.py              # URL configuration
│   └── ...
│
├── teams/                   # Django app for managing teams and players
│   ├── models.py            # Database models (Team, Player, Match, PointsTable)
│   ├── views.py             # Views for handling team and player data
│   ├── urls.py              # URLs specific to the teams app
│   ├── templates/           # HTML templates organized by app
│   │   └── teams/           # Templates specific to the teams app
│   └── ...
│
├── static/                  # Static files (CSS, images)
│   └── css/
│       └── styles.css       # CSS styles for the application
│
├── .env                     # Environment variables
├── .gitignore               # Git ignore file (ensures .env is not tracked)
├── manage.py                # Django's command-line utility
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Usage

### 1. Managing Teams and Players

- Teams: Use the Django admin panel to add, update, or delete teams. Each team has an identifier, name, logo, and club state.
- Players: Add players to teams, specifying their details such as jersey number, country, and performance history.


### 2. Viewing Data
- Teams List: Access the list of teams on the home page. Click on a team to view its details and list of players.
- Players List: View the details of players within each team, including their performance statistics.
- Match Fixtures: Generate and view random match fixtures between teams.
- Points Table: Access the points table to see the current standings of teams based on match results.

## Security Considerations

- Environment Variables: Sensitive information like SECRET_KEY and database credentials are stored in a .env file, ensuring they are not hard-coded in the project files.
- SQL Injection Protection: Django’s ORM handles SQL queries securely, reducing the risk of SQL injection.


## Testing

- Unit tests and TDD (Test-Driven Development) principles have been used to ensure the code is reliable and maintainable. To run the tests:

```
python manage.py test
```

## License

You can now save this content in a file named `README.md` in the root directory of your project. This file provides an organized and thorough guide for anyone who wants to use, develop, or deploy your Django-based Cricket Management System.
