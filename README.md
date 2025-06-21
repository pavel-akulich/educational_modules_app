# The application "Educational modules"


## Project Description
The application "Educational modules" is a backend part of an application created in the Python programming language using the Django REST framework.
This application is perfect for building any training platforms based on it.
The project includes a backend part responsible for data processing and business logic.

## Project Components

The project consists of the next components:

1. **Users Application:**
   - Contains a model for `User` users
   - Implemented the CRUD mechanism for the `User` model
   - In the file `tasks.py ` the task of sending notifications to users who have not logged into the application for a long time has been implemented

2. **Application educational_modules:**
   - Contains the module model `Module` and the lesson model `Lesson`
   - Contains a CRUD mechanism for model modules and lessons
   - Implemented pagination for the convenience of API requests and reducing the load on the server
   - Implemented logic that prohibits the user from creating lessons for other people's modules

## Technologies
   - The project is developed in the `Python` programming language using the `Django REST framework`
   - To work with the `PostgreSQL` database, a third-party library `psycopg2-binary` is used
   - `Celery` is used to perform periodic tasks (sending notifications)
   - `CORS` is configured for the project so that frontend can connect to the project on a deployed server
   - API documentation is connected to the project using the `drf-asg` library
   - For more stability the project is covered with automated unit tests
   - The `coverage` library is used to determine the test coverage of the project
   - The `poetry` tool is used to manage the virtual environment
   - The `python-dotenv` library is used to interact with environment variables
   - For easier and simpler deployment of the project is used containerization technology `Docker`

## Run the Project
   - Clone the repository https://github.com/pavel-akulich/educational_modules_app
   - Using the `docker compose up --build` command, assemble and run all the services
   - After successful completion of the previous step, the application will be available at http://localhost:8001/ or http://127.0.0.1:8001/

## API documentation
After the API server is successfully launched, the documentation will be available at the following addresses: http://localhost:8001/docs/ or http://localhost:8001/redoc/

## Notes
   - The project can be further developed and extended for broader use
   - The environment variables required for the project to work can be viewed in the `.env.sample` file
   - All the necessary dependencies are in the files `pyproject.toml` and `poetry.lock`

