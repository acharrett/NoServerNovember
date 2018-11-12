import urllib2
import json
from pprint import pprint

def handler(event=None,context=None):
    fortune_url='https://helloacm.com/api/fortune/'
    headers = { 'Accept': 'application/json', 'User-Agent': 'https://github.com/acharrett/NoServerNovember/tree/master/OneDirection' }
    fortune_req = urllib2.Request(fortune_url, headers=headers)
    fortune_resp = urllib2.urlopen(fortune_req).read()

    message = json.loads(fortune_resp)

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': message
            }
        }
    }

    return response

