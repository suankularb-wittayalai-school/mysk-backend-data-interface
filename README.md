# mysk-backend-fastapi-template

This repositary is used as a starting point for mysk backend fastapi services.

## Installation

### Source code

1. Clone the repo

```powershell
git clone https://github.com/suankularb-wittayalai-school/mysk-backend-fastapi-template.git
```

2. Create a virtual environment (optional)

```powershell
python -m virtualenv venv
venv\scripts\activate
```

3. Install dependencies

```powershell
pip install -r requirements.txt
```

4. Run the application

```powershell
python src/app.py
```

## Deployment

1. Pull the docker image

```powershell
docker pull ghcr.io/suankularb-wittayalai-school/mysk-backend-fastapi-template:latest
```

2. Run the docker image

```powershell
docker run -p 5000:5000 -d ghcr.io/suankularb-wittayalai-school/mysk-backend-fastapi-template:latest
```

**Note**: If you want to deploy the application along with a database we need to write your own docker-compose.yml file or setup a kubernetes cluster.
