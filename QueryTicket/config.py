base_url = "https://kyfw.12306.cn/otn/leftTicket/init"

query_url = "https://kyfw.12306.cn/otn/leftTicket/queryA"

price_url = "https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice"

seat_type_map = {
    "A9": "商务座",
    "M": "一等座",
    "O": "二等座",
    "A6": "高级软卧",
    "A4": "软卧",
    "F": "动卧",
    "A3": "硬卧",
    "A2": "软座",
    "A1": "硬座",
    "WZ": "无座"
}

seat_number_map = {
    "A9": 32,
    "M": 31,
    "O": 30,
    "A6": 21,
    "A4": 23,
    "F": 33,
    "A3": 28,
    "A2": 24,
    "A1": 29,
    "WZ": 26
}

error_code_map = {
    0: "查询成功",
    202201: "车次不能为空",
    202202: "查询不到车次的相关信息",
    202203: "出发站或到达站不能为空",
    202204: "查询不到结果",
    202205: "错误的出发站名称",
    202206: "错误的到达站名称",
    202207: "查询不到余票的相关数据",
    202208: "查询参数错误",
    202209: "请求12306网络错误, 请重试",
    202212: "查询出错"
}

with open("station2code.json", 'r') as fp:
    import json
    station2code_map = json.load(fp)