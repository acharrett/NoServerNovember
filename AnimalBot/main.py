import twitter
import configparser
import boto3
from pprint import pprint
import urllib.request

def handler(event=None, context=None):
    rekognition = boto3.client('rekognition')
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    dynamodb_table=dynamodb.Table('no-server-november')

    twitter_api = twitter_connect("twitter.conf")

    try:
        seen_id=dynamodb_table.get_item(Key={ 'id': 'imagebot-seen' })['Item']['data']
    except:
        seen_id="1"

    now_seen=None

    mentions = twitter_api.GetMentions(since_id=seen_id)

    for tweet in mentions:
        image_labels = []
        if tweet.media != None:
            for media in tweet.media:
                image_labels.append(get_image_label(rekognition,media.media_url_https))

        if len(image_labels) > 0:
            tweet_message = "@" + tweet.user.screen_name + " I see " + " ".join(image_labels)
            twitter_api.PostUpdate(tweet_message,in_reply_to_status_id=tweet.id)

        now_seen=tweet.id
            
    if now_seen != None:
        dynamodb_table.put_item(Item={ 'id': 'imagebot-seen', 'data': now_seen })

def get_image_label(rekognition,url):
    url_resp=urllib.request.urlopen(url)
    image_data = url_resp.read()
    rek_resp = rekognition.detect_labels(Image={ 'Bytes': image_data })
    top_label = rek_resp['Labels'][0]['Name'] 
    return top_label 

def twitter_connect(config_file_name):
    config = configparser.ConfigParser()
    config.read(config_file_name)

    twitter_api = twitter.Api(consumer_key=config.get("twitter","consumer_key"),
                              consumer_secret=config.get("twitter","consumer_secret"),
                              access_token_key=config.get("twitter","access_token"),
                              access_token_secret=config.get("twitter","access_token_secret"),
                              tweet_mode='extended')


    return twitter_api

