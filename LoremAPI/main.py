#!/usr/bin/python

import random
import json
import datetime

def handler(event,context):

    words_file="words"
    words_fh = open(words_file,'r')
    all_words = words_fh.read().split('\n')

    output_text = ""

    for i in xrange(50):
        output_text += random.choice(all_words) + " "

    api_output = {}
    api_output['random_text'] = output_text.rstrip(" ")
    api_output['generated_at'] = str(datetime.datetime.now())
    json_out = json.dumps(api_output)

    response = {
        "statusCode": 200,
        "headers": {
           'Content-type': 'application/json',
        },
        "body": json_out,
    }

    return response 
