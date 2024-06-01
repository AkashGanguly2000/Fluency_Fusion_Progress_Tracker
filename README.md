---

# Progress Tracking Microservice

The **Progress Tracking Microservice** is a component of the Habit Tracker App, designed to help users track their fitness activities, monitor progress, and achieve their health goals. This microservice is built using FastAPI and provides endpoints for logging and retrieving user progress data.

## Features

- **Customizable Progress Tracking:** Users can log various fitness activities, including duration, distance, intensity, and calories burned.
- **User Progress Retrieval:** Retrieve detailed progress data for individual users.
- **Dockerized Deployment:** Easily deploy the microservice using Docker.
- **Kubernetes Deployment:** Ready-to-use Kubernetes configuration for scalable deployments.

## Project Structure

```
progress-tracking/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── progress_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── progress.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── progress_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── progress_service.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── __init__.py
│   └── test_progress_service.py
├── Dockerfile
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── secret.yaml
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Kubernetes (optional, if you want to deploy it on a Kubernetes cluster)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/progress-tracking.git
   cd progress-tracking
   ```

2. **Set up a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application locally:**
   ```bash
   uvicorn app.main:app --reload
   ```

   The application should now be running locally on `http://127.0.0.1:8000`.

### Docker

1. **Build the Docker image:**
   ```bash
   docker build -t progress-tracking:latest .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -d -p 8000:8000 progress-tracking:latest
   ```

   The application should now be running in a Docker container and accessible at `http://127.0.0.1:8000`.

### Kubernetes

1. **Navigate to the kubernetes directory:**
   ```bash
   cd kubernetes/
   ```

2. **Deploy the application:**
   ```bash
   kubectl apply -f configmap.yaml
   kubectl apply -f secret.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

## Usage

### API Endpoints

- **POST /progress**
  - Description: Log a new progress entry.
  - Request Body:
    ```json
    {
      "user_id": int,
      "activity": "string",
      "duration": int,
      "distance": float,
      "intensity": int,
      "calories_burned": float,
      "date": "YYYY-MM-DD"
    }
    ```

- **GET /progress/{user_id}**
  - Description: Retrieve progress entries for a specific user.
  - Parameters: `user_id` (int)

### Example using `curl`

- **Log a new progress entry:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/progress" -H "Content-Type: application/json" -d '{
    "user_id": 1,
    "activity": "running",
    "duration": 30,
    "distance": 5.0,
    "intensity": 3,
    "calories_burned": 300,
    "date": "2023-05-21"
  }'
  ```

- **Retrieve progress entries for a specific user:**
  ```bash
  curl -X GET "http://127.0.0.1:8000/progress/1"
  ```

## Testing

Run unit tests with:
```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Kubernetes](https://kubernetes.io/)

---

This README provides an overview of the project, installation steps, usage instructions, and additional information like contributing and licensing. You can customize it further based on your project's specific details and requirements.
