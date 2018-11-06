import urllib2
import json
import twitter
import configparser

def handler(event, context):
    headers = { 'Accept': 'application/json', 'User-Agent': 'https://github.com/acharrett/NoServerNovember/tree/master/DadJoke' }
    joke_request = urllib2.Request('https://icanhazdadjoke.com/', headers=headers)
    joke_response = urllib2.urlopen(joke_request).read()
    joke_dict = json.loads(joke_response)

    twitter_api = twitter_connect("dadjoke.conf")

    twitter_api.PostUpdate(joke_dict['joke'])


def twitter_connect(config_file_name):
    config = configparser.ConfigParser()
    config.read(config_file_name)

    twitter_api = twitter.Api(consumer_key=config.get("twitter","consumer_key"),
                              consumer_secret=config.get("twitter","consumer_secret"),
                              access_token_key=config.get("twitter","access_token"),
                              access_token_secret=config.get("twitter","access_token_secret"),
                              tweet_mode='extended')


    return twitter_api
