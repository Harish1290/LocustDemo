from locust import HttpUser,TaskSet,task
import json
import request

class UserBehaviour(HttpUser)   :
    #task_set=Test_1

    min_wait=5000
    max_wait=9000 

    stop_timeout = 30

class Test_1(HttpUser):
    @task
    def users(self):
        response=self.client.post("/api/users",name="demo",json={
    "name": "1234",
    "job": "coder1"
    }
    )
        print(response.text)
        print(response.status_code)

       
        #json_var=response.json()
       # request_id=json_var['createdAt']
       # print('Post title is'+request_id)

        