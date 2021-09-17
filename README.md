# du.py
🦴 A Python API for Dangerous Users DB!

## Install
Just put in a terminal this simple command:
```sh
# For Linux
sudo pip3 install discord-du

# For others systems (Windows, MacOS...)
pip install discord-du
```

## Basic usage
```python
from dudb import DUapi

# Note: by default, it will look for discord.riverside.rocks website.
# If you want to change the instance, add the argument "url":
# du = DUapi(url = "https://discord.example.com")
du = DUapi(token="Your token")

# Get status of a user
print(du.getStatus("466262009256869889"))

# Report a user
du.report("466262009256869889", "He spammed my server")

# Get basic stats from the current instance
print(du.getStats())

# Delete all reports from the account where the API token was generated
du.deleteAllReports()

# Get the user whitelist of the current instance
print(du.getWhitelist())
```

## License
This repository is licensed under the [MIT License](./LICENSE).
