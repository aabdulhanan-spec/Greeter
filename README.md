# Greeter Docker App

A simple Python web application that displays a greeting in a browser.

## Run Locally

```bash
python app.py
```

Open:

http://localhost:8000

## Build Docker Image

```bash
docker build -t greeter:1.0 .
```

## Run Docker Container

```bash
docker run -d --name greeter-container -p 8000:8000 greeter:1.0
```

Open:

http://localhost:8000

## Docker Hub

Replace `YOUR_DOCKER_USERNAME` with your Docker Hub username.

```bash
docker tag greeter:1.0 YOUR_DOCKER_USERNAME/greeter:1.0
docker push YOUR_DOCKER_USERNAME/greeter:1.0
```

For version 1.1:

```bash
docker build -t greeter:1.1 .
docker tag greeter:1.1 YOUR_DOCKER_USERNAME/greeter:1.1
docker push YOUR_DOCKER_USERNAME/greeter:1.1
```
