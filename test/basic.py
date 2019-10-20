from locust import HttpLocust, TaskSet, task

def index(l):
    l.client.get("/?start_station=%E6%B1%89%E5%8F%A3&end_station=%E5%A8%81%E6%B5%B7&train_date=2019-10-17")

def stats(l):
    l.client.get("/")

def tast1(l):
    l.client.get("/?start_station=%E6%B1%89%E5%8F%A3&end_station=%E5%A8%81%E6%B5%B7&train_date=2019/10/17")


class UserTasks(TaskSet):
    # 列出需要测试的任务形式一
    tasks = [index, stats, task1]
    
class WebsiteUser(HttpLocust):
    host = "http://localhost:5000"
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks
