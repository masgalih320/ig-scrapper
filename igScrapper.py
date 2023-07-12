"""
    Project Name: Instagram Profile Scrapper
    Author: FDCI Galih
    Website: https://galihsptr.id
    GitHub: https://github.com/masgalih320
"""
# Import Library
from os import system
from bs4 import BeautifulSoup
import requests
import platform

# Check the OS
def checkOS():
    if platform.system() == "Linux":
        sys = "clear"
    elif platform.system() == "Windows":
        sys = "cls"
    else:
        print("OS Not supported")
        exit()
    return sys

# Get IG username from user input
print("--------------------------------------------")
print("Input example : galihsptr320")
print("--------------------------------------------")
def getInput():
    username = ""
    username = input("Input instagram username here: ")
    if username == "":
        system(checkOS())
        print("Please input instagram username")
        getInput()
    return username

# Data Parser
def parse(scrap):
    result = {}
    scrap = scrap.split("-")[0]
    scrap = scrap.split(" ")
    result['Followers'] = scrap[0]
    result['Following'] = scrap[2]
    result['Posts'] = scrap[4]
    return result

# Scrapping data
def scrap_data(username):
    req = requests.get("https://instagram.com/" + username)
    res = BeautifulSoup(req.text, "html.parser")
    meta = res.find("meta", property="og:description")
    return parse(meta.attrs['content'])

# Main Function
if __name__ == "__main__":
    try:
        data = scrap_data(getInput())
        print("Result:")
        print(data)

    except KeyboardInterrupt:
        print("\nCancelled by user")
        exit()
