import requests

class RequestError(Exception):
    def __init__(self, str):
        self.strerror = str

class DUapi:
    def __init__(self, token):
        self.token = token
        self.url = "https://discord.riverside.rocks"

    def checkStatus(self, id):
        r = requests.get(self.url + "/check.json.php", params={"id": id})
        if r.status_code == 200:
            return r.status_code
        else:
            raise RequestError("Bad request")