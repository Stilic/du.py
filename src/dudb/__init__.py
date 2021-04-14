import requests
import json
from types import SimpleNamespace

def parseJson(data):
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

class RequestError(Exception):
    """Exception for bad requests."""
    def __init__(self, str):
        self.strerror = str

class DUapi:
    def __init__(self, token, url = "https://discord.riverside.rocks"):
        self.token = token
        self.url = url

    def getStatus(self, id):
        """Checks status of a user and return a response code."""
        r = requests.get(self.url + "/check.json.php", params={"id": id})
        return r.status_code
    
    def report(self, id, reason):
        """Reports a user or raise a exception if you can't do this action."""
        r = requests.get(self.url + "/report.json.php", params={"id": id, "key": self.token, "details": reason})
        if r.status_code == 200:
            return r.status_code
        else:
            raise RequestError("You can't report this user")

    def getStats(self):
        """Returns basic statistics from the website."""
        r = requests.get(self.url + "/stats.json.php")
        return parseJson(r.json)

    def deleteAllReports(self):
        """Deletes all reports from the account who the API token was generated 
        or raise a exception if you can't do this action."""
        r = requests.get(self.url + "/delete.json.php", {"key": self.token})

    def getWhitelist(self):
        """Returns the user whitelist of the website."""
        r = requests.get(self.url + "/whitelist.json")
        return parseJson(r.json)
