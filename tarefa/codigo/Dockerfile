#FROM python:3.8-slim
FROM centos/python-36-centos7

COPY . /app

WORKDIR /app

# install dependencies
COPY requirements .
RUN pip install -r requirements

# Set env variables for Cloud Run
ENV PORT 80
ENV HOST 0.0.0.0

EXPOSE 80:80

CMD ["uvicorn", "main.py","--host", "0.0.0.0", "--port", "8000", "--reload"]
