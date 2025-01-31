# Predictive API - Dockerized Machine Learning Model

## Overview

This project is a **FastAPI-based machine learning API** that utilizes a **Decision Tree Classifier** to make predictions based on input data. The API is fully Dockerized, allowing easy deployment and scalability.

## Features

- FastAPI-based RESTful API
- Decision Tree Classifier for predictions
- Dockerized for containerized execution
- Exposed endpoints for predictions

## Prerequisites

Ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Postman](https://www.postman.com/downloads/) (for API testing, optional)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/predictive-api.git
cd predictive-api
```

### 2. Install Dependencies (Optional for local testing)

```bash
pip install -r requirements.txt
```


## Running with Docker

### 1. Build the Docker Image

```bash
docker build -t your_dockerhub_username/predictive-api .
```

### 2. Run the Docker Container

```bash
docker run -p 8000:8000 your_dockerhub_username/predictive-api
```

## API Endpoints

### 1. **Root Endpoint** (Welcome message)

- **GET** `/`
- **Response**:

```json
{
  "message": "Welcome to the Predictive Model API!"
}
```

### 2. **Prediction Endpoint**

- **POST** `/predict/`
- **Request Body (JSON):**

```json
{
  "input_value": 3.5
}
```

- **Response:**

```json
{
  "input": 3.5,
  "prediction": 1
}
```


