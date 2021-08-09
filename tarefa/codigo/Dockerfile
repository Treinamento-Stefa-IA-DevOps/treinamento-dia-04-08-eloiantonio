#FROM python:3.8-slim
FROM centos/python-36-centos7

COPY . /codigo

WORKDIR /codigo

CMD ["uvicorn", "main:codigo","--host", "0.0.0.0", "--port", "80", "--reload"]
