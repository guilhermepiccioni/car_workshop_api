# FastAPI Car Services Request API

This is an API built with FastAPI to manage car services requests. It provides CRUD (Create, Read, Update, Delete) operations for services request entities.
## Technologies used
- Python 3.9
- PostgreSQL
- Docker
- FastAPI
- SQLAlchemy
- PgAdmin

## Prerequisites

- [Docker](https://www.docker.com/) installed

## Environment Setup

1. Clone this repository:

```bash
git clone <YOUR_REPOSITORY_URL>
```
## API Routes
- http://localhost:8000/docs - Swagger UI to explore and interact with the API.
- http://localhost:8000/redoc - ReDoc for a more user-friendly documentation.

## Main Endpoints
```
POST /services_requests/: Create a new service request.
GET /services_requests/: Get all services requests with optional filtering.
GET /services_requests/{request_id}: Get details of a specific service request.
PATCH /services_requests/{request_id}: Update an existing service request.
```
## Project Structure
### The project is structured as follows:

  - app/main.py: Main file of the FastAPI application.
  - app/database/database.py: Database configuration and table creation.
  - app/api/routes/routes.py: Definition of API routes.
  - app/models/models.py: Definition of data models using SQLAlchemy and Pydantic.
  - Dockerfile: Configuration to build the Docker image of the application.
  - docker-compose.yml: Docker Compose configuration for container orchestration.
  - Makefile: Set of Make commands to facilitate local environment execution and cleanup.

## Start the project
```
make run
```

## Local Cleanup

- To stop Docker container execution and clean volumes, use the command:

```
make cleanup_local
# This command removes all local containers, volumes, and orphans.
```

### General Cleanup
- For a more comprehensive cleanup, including the removal of images and system cache, use the command:
```
make cleanup
# This command removes all containers, images, volumes, and performs a system cache cleanup.
```
