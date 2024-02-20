## FastAPI Template With MYSQL

FastAPI repository that uses MYSQL and Alembic. Inspired by [Grey-A Heavyweight FastAPI Template](https://github.com/Grey-A/heavyweight-fastapi).

### Project Structure

```
.vscode
alembic/
app/
    config/
        __init__.py
        database.py
        settings.py
    example_module/
        __init__.py
        apis.py
        models.py
        schemas.py
        selectors.py
        services.py
    __init__.py
    dependencies.py
    main.py
.gitignore
alembic.ini
env_sample.txt
main.py
poetry.toml
railway.toml
README.md
```

### Components

**.vscode:** Configuration files for Visual Studio Code.

**alembic/:** Contains Alembic settings and migrations.

**env_sample.txt:** Sample environment variable list. Create a `.env` file and provide values.

**main.py:** Entry point for the poetry run script.

**config/:** Holds project settings.

- **database.py:** Manages database connection, session settings, and the base database model.
- **settings.py:** Utilizes pydantic_settings to load environment variables. Change the `SECRET_KEY` from the default value on Railway.

**app/:** The main FastAPI project directory.

- **main.py:** Entry point of the application, with a router linking to the `user/` module.
- **dependencies.py:** Initializes the database session.
- **user/:** Contains code and functionality related to users.
  - **apis.py:** Houses endpoints like `user_create`, `user_login`, and `user_details`.
  - **models.py:** Uses SQLAlchemy to draft the user table. Alembic handles migrations.
  - **schemas.py:** Defines schemas for create, details, login, and token requests.
  - **selectors.py:** Manages GET operations, fetching data from the database.
  - **services.py:** Handles POST, PUT, PATCH, and DELETE operations, manipulating database data.

### Getting Started

1. Setup Poetry

   Create the poetry environment

   ```
   poetry env use 3.11
   ```

   Start the poetry shell

   ```
   poetry shell
   ```

2. Install dependencies:

   ```
   poetry install
   ```

3. Create a `.env` file and input environment variables.

4. Initialize database tables:

   ```
   alembic upgrade head
   ```

5. Start the application in development mode:

   ```
   poetry run dev
   ```

6. Test the application by making requests to endpoints.

### Contribute to the Project

We welcome contributions from the community to make this FastAPI Starter Template even better. If you have ideas for improvements, new features, or bug fixes, feel free to:

- Fork the repository and create a new branch for your contribution.
- Submit pull requests to propose changes to the project.
- Engage in discussions and share your thoughts on enhancements.

For detailed information, refer to the following resources:

- FastAPI documentation: https://fastapi.tiangolo.com/
- Alembic documentation: https://alembic.sqlalchemy.org/en/latest/
- Poetry documentation: https://python-poetry.org/docs/
