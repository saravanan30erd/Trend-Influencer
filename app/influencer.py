from tweepy import Cursor
from functools import partial
import datetime
import time
from authentication import *
from top_trends import top_trends
from multiprocessing import Pool, Queue
from db_operations import update_document
from woeids import get_woeids

def search_tweet(api_key, auth_key, location, trend):
    """ """
    #Authentication
    api = api_key(auth_key)
    dic = {}
    for tweet in Cursor(api.search, q=trend, lang='en').items(500):
        if tweet.user.screen_name not in dic:
            if tweet.user.followers_count > 2000:
                dic[tweet.author.screen_name] = [
                        tweet.author.followers_count, tweet.author.friends_count, tweet.author.statuses_count, tweet.author.name, tweet.text, tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"), tweet.author.location, tweet.author.created_at.strftime("%Y-%m-%d %H:%M:%S"), tweet.author.description]

    #Sorting the keys based on values
    count = 0 #Get only top 10 influencers
    influencer_list = []
    for key in sorted(dic, key=dic.__getitem__, reverse=True):
        if count < 10:
            count += 1
            influencer_details = {}
            filter1 = {}
            filter1['_id'] = key
            influencer_details['_id'] = key
            influencer_details['screen_name'] = key
            influencer_details['Name'] = dic[key][3]
            influencer_details['Description'] = dic[key][8]
            influencer_details['created_at'] = dic[key][7]
            influencer_details['Location'] = dic[key][6]
            influencer_details['Followers'] = dic[key][0]
            influencer_details['Tweets'] = dic[key][2]
            influencer_details['Following'] = dic[key][1]
            update_document('influencers', influencer_details, filter1) 
            influencer_records = {}
            influencer_records['screen_name'] = key
            influencer_records['tweet'] = dic[key][4]
            influencer_records['tweet_created_at'] = dic[key][5]
            influencer_list.append(influencer_records)
    trend_details = { '_id' : trend, 'trend_topic' : trend, 'location' : location, 'datetime' : datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), 'influencers' : influencer_list}
    filter2 = {}
    filter2['_id'] = trend
    update_document('trends', trend_details, filter2)

def main():
    while True:
        woeids = get_woeids()
        for key,item in woeids.iteritems():
            pool = Pool(processes=4)
            trends = top_trends(item)
            location = key
            trends_1,trends_2 = trends[:len(trends)/2],trends[len(trends)/2:]
            try:
                func = partial(search_tweet, api_auth_key, 'key1', location)
                pool.map(func, trends_1)
            except Exception, e:
                print str(e)

            try:
                func = partial(search_tweet, api_auth_key, 'key2', location)
                pool.map(func, trends_2)
            except Exception, e:
                print str(e)
            finally:
                pool.close()
                pool.join()
                time.sleep(1800)

if __name__ == '__main__':
    main()
