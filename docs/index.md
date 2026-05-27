# Python App

## Overview

This is a Flask-based Python application registered in Backstage.

## Features

- Flask API
- Docker support
- Kubernetes deployment
- GitHub Actions CI/CD

## Architecture

Frontend -> API -> Database

## Deployment

```bash
docker build -t python-app .
docker run -p 5000:5000 python-app