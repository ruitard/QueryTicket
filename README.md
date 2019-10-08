# QueryTicket
提供12306车票查询的微服务程序



请求参数说明:

| 名称          | 必填 | 类型   | 说明                       |
| ------------- | ---- | ------ | -------------------------- |
| start_station | 是   | string | 出发站名称                 |
| end_station   | 是   | string | 到达站名称                 |
| train_date    | 否   | string | 乘车日期, 格式: 2019-12-12 |

使用样例: 

```
www.example.com?start_station=汉口&end_station=威海&train_date=2019-12-12
```



返回json对象参数说明:

| 名称               | 类型   | 说明         |
| ------------------ | ------ | ------------ |
| train_name         | string | 车次名称     |
| start_station      | string | 出发站名称   |
| start_station_type | string | 出发站类型   |
| end_station        | string | 到达站名称   |
| end_station_type   | string | 到达站类型   |
| start_time         | string | 出发时间     |
| end_time           | string | 到达时间     |
| run_time           | string | 运行时间     |
| seat_list          | array  | 座位信息列表 |
| seat_type          | string | 座位类型     |
| price              | string | 票价         |
| left_ticket        | string | 有\|无\|票数 |

返回样例:

```json
{
  "result": [
    {
      "end_station": "威海",
      "end_station_type": "终",
      "end_time": "18:54",
      "run_time": "10:04",
      "seat_list": [
        {
          "left_ticket": "有",
          "price": "¥758.5",
          "seat_type": "二等座"
        },
        {
          "left_ticket": "9",
          "price": "¥1224.0",
          "seat_type": "一等座"
        },
        {
          "left_ticket": "10",
          "price": "¥2358.0",
          "seat_type": "商务座"
        }
      ],
      "start_station": "武汉",
      "start_station_type": "始",
      "start_time": "08:50",
      "train_name": "G2082"
    },
    {
      "end_station": "威海",
      "end_station_type": "终",
      "end_time": "08:01",
      "run_time": "20:41",
      "seat_list": [
        {
          "left_ticket": "有",
          "price": "¥156.5",
          "seat_type": "硬座"
        },
        {
          "left_ticket": "1",
          "price": "¥422.5",
          "seat_type": "软卧"
        },
        {
          "left_ticket": "有",
          "price": "¥268.5",
          "seat_type": "硬卧"
        },
        {
          "left_ticket": "有",
          "price": "¥156.5",
          "seat_type": "硬座"
        },
        {
          "left_ticket": "有",
          "price": "¥156.5",
          "seat_type": "无座"
        }
      ],
      "start_station": "汉口",
      "start_station_type": "始",
      "start_time": "11:20",
      "train_name": "K1068"
    }
  ]
}
```



自定义状态码说明

| 错误码 | 说明                         |
| ------ | ---------------------------- |
| 202201 | 车次不能为空                 |
| 202202 | 查询不到车次的相关信息       |
| 202203 | 出发站或终点站不能为空       |
| 202204 | 查询不到结果, result为空数组 |
| 202205 | 错误的出发站名称             |
| 202206 | 错误的到达站名称             |
| 202207 | 查询不到余票相关数据哦       |
| 202208 | URL参数名称错误              |
| 202209 | 请求12306网络错误,请重试     |
| 202212 | 查询出错                     |

