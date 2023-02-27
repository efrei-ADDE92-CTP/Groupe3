from flask import Flask
from locust import HttpUser, task

app = Flask(__name__)

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/predict", data='{"sepal_length": 5.1,"sepal_width": 3.5,"petal_length": 1.4,"petal_width": 0.2}')
        
if __name__ == '__main__':
    app.run(port=8000, debug=True)
    
