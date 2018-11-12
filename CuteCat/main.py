#!/usr/bin/python

import giphy_client
from giphy_client.rest import ApiException
import os
import random

def handler(event=None, context=None):
    api_key=os.environ['GIPHY_API_KEY']
    giphy_api = giphy_client.DefaultApi()
    query = 'back to the future'
    lang = 'en'
    fmt = 'json'
    gif_url=""

    api_resp = giphy_api.gifs_search_get(api_key, query, limit=50, offset=0, rating='g', lang=lang, fmt=fmt)

    random_int = random.randint(0,49)

    gif_url=api_resp.data[random_int].images.downsized_large.url

    body_text = gen_html_body(gif_url)
    print gif_url

    response = {
        "statusCode": 200,
        "headers": {
           'Content-type': 'text/html',
           'Cache-Control': 'no-store, no-cache, must-revalidate',
        },
        "body": body_text,
    }

    return response 

def gen_html_body(gif_url):
    body_text = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'
    body_text += '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">\n'
    body_text += '<head>\n'
    body_text += '<meta http-equiv="Content-Type" content="text/htmlcharset=utf-8" />\n'
    body_text += '<title>#noServerNovember</title></head>\n'
    body_text += '<body><h2><center>Great Scott, it\'s <a href="https://serverless.com/blog/no-server-november-challenge/">#noServerNovember</a>!</center></h2>\n'
    body_text += '<center><img src="' + gif_url + '"></center>\n'
    body_text += '</body></html>\n'


    return body_text

