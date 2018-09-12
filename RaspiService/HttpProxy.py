import requests
import json

class HttpProxy(object):
    def __init__(self, url):
        self.url = url
    
    def InformServoStatus(self, dto):
        headers = {"Content-Type": "application/json"}
        print("Llamando al servicio.")
        data = json.dumps(dto)
        print(self.url)
        res = requests.post(self.url, data, headers=headers)
        print(res)
        return res