from flask import Flask
from flask import request
import requests 
import time 

import config 

app = Flask(__name__)

rcookies = requests.get(config.base_url).cookies
config.cookies = {key: rcookies[key] for key in rcookies.keys()}

@app.route('/', methods=["GET"])
def hello_world():
    ret = dict()
    params = {
        "leftTicketDTO.train_date": config.train_date,
        "leftTicketDTO.from_station": config.from_station,
        "leftTicketDTO.to_station": config.to_station,
        "purpose_codes": "ADULT"
    }
    r = requests.get(config.query_url, params=params, cookies=config.cookies)
    data = r.json()["data"]
    
    config.station_map = data["map"]
    # config.train_date = train_date

    result = data["result"]
    result = tuple(map(handler, result))
    ret["error_code"] = 0
    ret["reason"] = config.error_code_map[ret["error_code"]]
    ret["result"] = result
    return ret 

def handler(train: str) -> dict:
    train = train.split('|')
    ret = dict()
    ret["train_name"] = train[3]
    ret["start_station"] = config.station_map[train[6]]
    ret["start_station_type"] = "始" if train[4] == train[6] else "过"
    ret["end_station"] = config.station_map[train[7]]
    ret["end_station_type"] = "终" if train[5] == train[7] else "过"
    ret["start_time"] = train[8]
    ret["end_time"] = train[9]
    ret["run_time"] = train[10]
    seat_list = list()

    seat_types = train[35]
    params = {
        "train_no": train[2],
        "from_station_no": train[16],
        "to_station_no": train[17],
        "seat_types": seat_types,
        "train_date": config.train_date
    }
    r = requests.get(config.price_url, params=params, cookies=config.cookies)
    price_data = r.json()["data"]
    for c in seat_types:
        seat_info = dict()
        c = "A{}".format(c) if c.isdigit() else c 
        seat_info["seat_type"] = config.seat_type_map[c]
        seat_info["left_ticket"] = train[config.seat_number_map[c]]
        seat_info["price"] = price_data[c]
        seat_list.append(seat_info)
    if seat_types.count('1') > 1 or seat_types.count('O') > 1:
        c = "WZ"
        seat_info = dict()
        seat_info["seat_type"] = config.seat_type_map[c]
        seat_info["left_ticket"] = train[config.seat_number_map[c]]
        seat_info["price"] = price_data[c]
        seat_list.append(seat_info)

    ret["seat_list"] = seat_list
    return ret 

@app.before_request
def prepare():
    if "start_station" not in request.args:
        return "", "202208", {"reason": "参数错误"}
    if "end_station" not in request.args:
        return "", "202208", {"reason": "参数错误"}
    start = request.args["start_station"]
    end = request.args["end_station"]
    if start not in config.station2code_map:
        return "", "202205", {"reason": "出发站名称错误"}
    if end not in config.station2code_map:
        return "", "202206", {"reason": "到达站名称错误"}
    config.from_station = config.station2code_map[start]
    config.to_station = config.station2code_map[end]
    if "train_date" in request.args:
        try:
            time.strptime(request.args["train_date"], "%Y-%m-%d")
        except:
            return "", "202210", {"reason": "时间格式错误"}
    config.train_date = request.args.get("train_date", time.strftime("%Y-%m-%d", time.localtime()))

if __name__ == "__main__":
    app.run()