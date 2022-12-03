import requests
import env_vars
import os 
from os.path import exists

def import_data(year,day):
    # Get Request
    url ="https://adventofcode.com/{year}/day/{day}/input"
    auth = {"session": env_vars.token}
    USER_AGENT = {"User-Agent": env_vars.message}
    response = requests.get(url, cookies=auth, headers=USER_AGENT)
    data = response.text
    print(response.status_code)
    print(data)

    # Write to file
    path = os.path.dirname(os.path.abspath(__file__)) + "/day" + str(day) + ".txt"

    if response.status_code == 200 and not exists(path):
        with open(path, "w") as text_file:
            text_file.write(data)


# Change variables as needed
year = 2022
day = 3

import_data(year,day)