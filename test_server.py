# -*- coding:utf-8 -*-

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import random
# import threading


def json_data():
    earth_json = {
        "configUpdated": False,
        "dnsServer": "0.0.0.0",
        "gateway": "0.0.0.0",
        "ip": "10.10.0.2",
        "linkQuality": [
            [
                -10,
                22,
                22
            ],
            [
                21,
                -10,
                22
            ],
            [
                21,
                21,
                -10
            ]
        ],
        "nodeInfos": [
            {
                "id": 1,
                "ip": "10.10.0.2",
                "latitude": -90.0,
                "longitude": -180.0
            },
            {
                "id": 2,
                "ip": "10.10.0.3",
                "latitude": -90.0,
                "longitude": -180.0
            },
            {
                "id": 8,
                "ip": "10.10.0.2",
                "latitude": -90.0,
                "longitude": -180.0
            }
        ],
        "nodeNumber": 3,
        "nwMask": "255.255.255.0",
        "operatingFreq": 1,
        "selfId": 8,
        "speakingNodes": [],
        "temp": 60.2899780272
    }

    while True:
        latitude0 = round(random.uniform(31.40, 31.50), 4)
        longitude0 = round(random.uniform(121.20, 121.30), 4)
        latitude1 = round(random.uniform(31.40, 31.50), 4)
        longitude1 = round(random.uniform(121.20, 121.30), 4)
        latitude2 = round(random.uniform(31.40, 31.50), 4)
        longitude2 = round(random.uniform(121.20, 121.30), 4)

        # 如果随机经纬相同重新随机
        if latitude0 == latitude1 or latitude1 == latitude2:
            continue
        elif longitude0 == longitude1 or longitude1 == longitude2:
            continue
        else:
            break

    earth_json['nodeInfos'][0]['latitude'] = latitude0
    earth_json['nodeInfos'][0]['longitude'] = longitude0
    earth_json['nodeInfos'][1]['latitude'] = latitude1
    earth_json['nodeInfos'][1]['longitude'] = longitude1
    earth_json['nodeInfos'][2]['latitude'] = latitude2
    earth_json['nodeInfos'][2]['longitude'] = longitude2

    return earth_json


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path != "/status":
            self.send_response(404)
            self.send_header("Content-Type", "text/html;charset=utf-8")
            self.send_header("Content-Length", str(len("params is wrong")))
            self.end_headers()
            self.wfile.write("params is wrong".encode())

            # self.finish()
            # self.connection.close()
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/json;charset=utf-8")
        message = json.dumps(json_data(), ensure_ascii=False).encode('utf-8')
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)

        # self.finish()
        # self.connection.close()
        return


if __name__ == '__main__':
    server = ThreadingHTTPServer(('0.0.0.0', 80), RequestHandler)
    server.serve_forever()
