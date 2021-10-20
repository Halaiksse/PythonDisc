import requests, math # We also import the maths library because it provides some functions we need
from datetime import datetime

#Although this module is not implemented yet, it will be in later versions/when the API is actually stable
Fileapi = open("c:\\python\\APIHYPIXEL.txt", "r")
APILIST = []
APILIST = Fileapi.readlines()

API_KEY = APILIST[0] # Replace with your API key

# These are just values used to calculate the level (don't worry about them too much)
BASE = 10_000
GROWTH = 2_500
REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
REVERSE_CONST = REVERSE_PQ_PREFIX
GROWTH_DIVIDES_2 = 2 / GROWTH







def get_level(name):
    url = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None
    exp = int(data["player"]["networkExp"]) 
    return math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))

def get_karma(name):
    url = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
    res = requests.get(url)
    data = res.json()
    if data["player"] is None:
        return None
    karma = int(data["player"]["karma"])
    return karma









