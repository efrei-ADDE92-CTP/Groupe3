from flask import Flask
from locust import HttpUser, task
import random

app = Flask(__name__)

class HelloWorldUser(HttpUser):
    @task
    def load_charge(self):
        self.client.post("predict", data='{"sepal_length": '+ str(random.uniform(0, 10))+ ',"sepal_width":'+ str(random.randrange(0, 10))+',"petal_length":'+ str(random.uniform(0, 10))+',"petal_width": '+ str(random.uniform(0, 10))+'}')
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
