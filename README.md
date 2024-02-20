# 🚀 Django Messaging App

## Table of Contents


- [Overview](#overview)
- [Local Setup 👨‍💻](#local-setup)
    - [Virtual Environment Setup](#virtual-environment-setup)
        - [On Linux](#on-linux)
        - [On Windows](#on-windows)
    - [Installing Dependencies And Run Server](#installing-dependencies-and-run-server)
- [Docker Setup 🐳](#docker-setup-🐳)
- [API Documentation](#api-documentation)
  - [Swagger Endpoints](#swagger-endpoints)
  - [User Endpoints](#user-endpoints)
  - [Messaging Endpoints](#messaging-endpoints)

## Overview

Django Messaging App is a simple messaging application built with Django REST Framework. It provides a RESTful API for user management and messaging functionality.

**Features:**
1. The user can create an account using username and password.
2. Users can message each other using username.
3. Users can access their messaging(inbox, outbox).

**Testing Endpoints:**
- To test the API endpoints, you can use [Swagger](http://127.0.0.1:8000/swagger/) for a user-friendly interactive documentation.
- Alternatively, you can import the [Postman collection](messaging_service.postman_collection.json) provided in the repository and try the endpoints in Postman.

**API Flow:**
1. **Create User:**
   - Use the `/api/v1/user/register/` endpoint to create a new user by providing a username and password.

2. **Obtain Token:**
   - Use the `/api/v1/user/token/` endpoint to obtain a JWT token by providing user credentials (username and password).
   - The response will include an access token.

3. **Access Other Endpoints:**
   - Use the obtained access token as the Authorization header (`"Bearer + access_token"`) for other user-related and messaging endpoints.
   - Example endpoints include `/api/v1/user/list-update/`, `/api/v1/messaging/send-message/`, etc.

## Getting Started

## Local Setup

1. Clone the repository and move the-project-directory :

    ```bash
    git clone https://github.com/Mohamad-Aboda/messaging-service
    cd messaging-service
    ```
## Virtual Environment Setup

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - ### On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - ### On Linux:

        ```bash
        source venv/bin/activate
        ```

## Installing Dependencies And Run Server

4. Install dependencies 

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
6. Run server:

    ```bash
    python manage.py runserver
    ```
    The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Docker Setup 🐳

To build and run the Django Messaging App using Docker, follow these steps:

1. Build the Docker image:

    ```bash
    make build
    ```

2. Start the Docker containers:

    ```bash
    make up
    ```

    Alternatively, you can combine both steps with a single command:

    ```bash
    make build-up
    ```

    The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Additional Docker Commands:

- To stop and remove Docker containers:

    ```bash
    make down
    ```

Make sure to have Docker and Docker Compose installed before running these commands. If you encounter any issues, refer to the [Local Setup](#local-setup) section for alternative methods.

Feel free to adjust the instructions based on your specific needs or provide more details if necessary.


# API Documentation

Django Messaging App is a simple messaging application built with Django and Django REST Framework.

Explore the API using <b>Swagger<b> Tool.:

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Swagger Endpoints

| Tool         | Endpoint                         | Description                          |
|--------------|----------------------------------|--------------------------------------|
| Swagger UI   | [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)   | Swagger UI Documentation            |
| ReDoc        | [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)       | ReDoc API Explorer                  |

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## User Endpoints


| Method | Endpoint                  | Description           | Body                        | Header               | Response            |
|--------|---------------------------|-----------------------|-----------------------------|----------------------|---------------------|
| POST   | `/api/v1/user/register/`    | Register a new user   | (username, password) | -                    | New user data       |
| POST   | `/api/v1/user/token/`        | Obtain JWT token          | User credentials (username, password) | -                    | JWT tokens          |
| POST   | `/api/v1/user/token/refresh/`| Refresh JWT token         | Refresh token               | -                    | New access token    |
| GET    | `/api/v1/user/all-users/`   | List all users        | -                           | -  | List all users       |
| GET    | `/api/v1/user/list-update/`      | Get user information  | -                           | Authorization token <br>"Bearer + access_token" | User information    |
| PUT    | `/api/v1/user/list-update/`      | Update user information | Updated user data (username, password) | Authorization token <br>"Bearer + access_token" | Updated user data |
| PATCH  | `/api/v1/user/list-update/`      | Partially update user information | Partial user data (username, password) | Authorization token <br>"Bearer + access_token" | Updated user data |

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Messaging Endpoints

| Method | Endpoint                  | Description           | Body                        | Header               | Response            |
|--------|---------------------------|-----------------------|-----------------------------|----------------------|---------------------|
| POST   | `/api/v1/messaging/send-message/`     | Send a message        | Message data (text, receiver_username) | Authorization token <br>"Bearer + access_token" | Success message     |
| GET    | `/api/v1/messaging/inbox/`    | Get inbox messages for the authenticated user | - | Authorization token <br>"Bearer + access_token" | List of inbox messages |
| GET    | `/api/v1/messaging/outbox/`   | Get outbox messages for the authenticated user | - | Authorization token <br>"Bearer + access_token" | List of outbox messages |

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

