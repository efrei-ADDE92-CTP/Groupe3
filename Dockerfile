# syntax=docker/dockerfile:1
FROM python:alpine3.16
WORKDIR /usr/src/app

RUN pip install  --no-cache-dir -r requirements.txt

# install app
COPY requirements.txt requirements.txt
COPY API_flask.py API_flask.py
COPY knn_Iris.pkl knn_Iris.pkl

# final configuration
ENV FLASK_APP=API_flask
EXPOSE 8000
  CMD [ "python3", "API_flask.py"]

