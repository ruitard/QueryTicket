import redis
import json

with open("station2code.json", 'r') as fp:
    data = json.dump(fp)
    
r = redis.Redis(host="localhost", port=6379, db=0)
r.mset(data)