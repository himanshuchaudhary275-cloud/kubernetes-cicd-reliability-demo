# Kubernetes CI/CD Reliability Demo

A minimal production-style application stack demonstrating containerization,
Kubernetes deployment, CI/CD automation, reliability engineering, and
operational debugging.

## Project Overview

This project deploys a Python Flask backend and Redis dependency to a
Kubernetes cluster running on Minikube.

The project demonstrates:

- Docker containerization
- Kubernetes Deployments and Services
- Redis service dependency
- Rolling updates
- Readiness and liveness probes
- CPU and memory resource requests/limits
- GitHub Actions CI/CD
- Self-hosted GitHub Actions runner
- Intentional failure simulation
- Kubernetes troubleshooting and recovery

## Architecture

```text
Developer
   |
   | git push
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   v
Self-hosted Windows Runner
   |
   +----------------------+
   |                      |
   v                      v
Docker Build          kubectl / Minikube
   |                      |
   |                      v
   |                 Kubernetes
   |                  namespace: demo
   |                      |
   |              +-------+-------+
   |              |               |
   |              v               v
   |          Backend x2        Redis x1
   |          Port 5000        Port 6379
   |              |
   |              +-------> Redis
   |
   +----> Minikube image load