from pprint import pprint
import json
import urllib2

def handler(event,context):
    reply_text = get_fact()

    result = {}
    result['response_type'] = 'in_channel'
    result['text'] = reply_text
    result_json = json.dumps(result)

    response = {
        "statusCode": 200,
        "headers": {
           'Content-type': 'application/json',
        },
        "body": result_json,
    }

    return response

def get_fact():
    request_url = 'https://catfact.ninja/facts'

    headers = { 'Accept': 'application/json', 'User-Agent': 'https://github.com/acharrett/NoServerNovember/tree/master/CatFacts' }
    fact_request = urllib2.Request(request_url, headers=headers)
    fact_response = urllib2.urlopen(fact_request).read()
    cat_facts = json.loads(fact_response)

    return cat_facts['data'][0]['fact']
