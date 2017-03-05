from get_woeid import get_woeid
from authentication import *
from sys import argv as ARG

def top_trends_by_country(Country, Region):
    #Authentication
    api = api_auth_key('key2') 
    trends_list = []
    #Get woeid
    woeid = get_woeid(Country, Region)
    trends = api.trends_place(id=int(woeid), lang='en')
    count = 0
    for trend in trends[0]['trends']:
        if count < 10:
            trends_list.append(trend['name'])
            count += 1
    return trends_list
            

def top_trends(woeid):
    #Authentication
    api = api_auth_key('key2') 
    trends_list = []
    trends = api.trends_place(id=int(woeid), lang='en')
    count = 0
    for trend in trends[0]['trends']:
        if count < 10:
            trends_list.append(trend['name'])
            count += 1
    return trends_list
            

if __name__ == '__main__':
    print top_trends(ARG[1])
