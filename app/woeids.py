from authentication import *

def get_woeids():
    api = api_auth_key('key1')
    #Get all locations where twitter provides trends
    world_trends = api.trends_available(_woeid=1)

    #Find the woeids for Country India
    woeids = {} 
    for t in world_trends:
        if t['countryCode'] == 'IN':
            woeids[t['name']] = t['woeid']
    return woeids

if __name__ == "__main__":
    print get_woeids()    
    
