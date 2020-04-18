from locust import HttpLocust, TaskSet, task, between
import json

class UserBehavior(TaskSet):

    @task(1)
    def create_post(self):
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        self.client.post("/posts",data= json.dumps({
            "title": "foo",
            "body": "bar",
            "userId": 1
        }),
        headers=headers,
        name = "Create a new post")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 15)