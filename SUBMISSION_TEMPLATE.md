# Assignment Submission

## 1. GitHub Repository

GitHub Repository:
PASTE YOUR GITHUB REPOSITORY LINK HERE

## 2. Git Commit Graph

Run:

```bash
git log --oneline --graph --all --decorate
```

Paste the actual output here.

## 3. Docker Hub Image

Docker Hub Image:

YOUR_DOCKER_USERNAME/greeter

Versions:
- YOUR_DOCKER_USERNAME/greeter:1.0
- YOUR_DOCKER_USERNAME/greeter:1.1

Docker Hub Link:
PASTE YOUR DOCKER HUB REPOSITORY LINK HERE

## 4. Part 5 Answer

Nginx came from the official Nginx Docker image, which Docker downloaded when I ran the Nginx container. It was running inside the Docker container, not installed directly on my computer. After I stopped and removed the Nginx container, the running Nginx container was removed. The Docker image may still remain locally unless it is separately removed or pruned.
