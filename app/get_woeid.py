from authentication import *
from sys import argv as ARG

"""
    Find the location woeid from location name
    python get_woeid.py <countrycode> <location>
    e.g python get_woeid.py IN Chennai 
"""
def get_woeid(CC, loc):
    api = api_auth_key('key2')
    #Get all locations where twitter provides trends
    world_trends = api.trends_available(_woeid=1)

    #Find the woeid 
    for t in world_trends:
        if t['countryCode'] == CC and t['name'] == loc:
            return t['woeid']


if __name__ == "__main__":
    woeid = get_woeid(ARG[1], ARG[2])
    print woeid

