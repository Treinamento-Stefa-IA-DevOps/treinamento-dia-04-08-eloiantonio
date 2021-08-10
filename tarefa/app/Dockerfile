#FROM python:3.8-slim
FROM centos/python-36-centos7

COPY . /app

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main.py","--host", "0.0.0.0", "--port", "80", "--reload"]
