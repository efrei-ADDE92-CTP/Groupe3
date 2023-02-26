# syntax=docker/dockerfile:1
FROM python:3.8-slim
WORKDIR /usr/src/app


# install app
COPY requirements.txt requirements.txt
COPY API_flask.py API_flask.py
COPY knn_Iris.pkl knn_Iris.pkl
COPY . .

RUN pip install  --no-cache-dir -r requirements.txt


# final configuration
ENV FLASK_APP=API_flask
EXPOSE 8000
  CMD [ "python3", "API_flask.py"]

