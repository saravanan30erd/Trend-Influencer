from tweepy import *
import ConfigParser

def config_dict():
    parser = ConfigParser.ConfigParser()
    parser.read('config.ini')
    config = {}
    for group in parser.sections():
        config.setdefault(group, {})
        for key, value in parser.items(group):
            config[group][key] = value
    return config
 
def api_auth_key(key):
    """ Authentication """
    config = config_dict()
    auth = OAuthHandler(config[key]['cons_tok'], config[key]['cons_sec'])
    auth.set_access_token(config[key]['app_tok'], config[key]['app_sec'])
    api = API(auth)
    return api
