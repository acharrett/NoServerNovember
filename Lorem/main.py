import json
import urllib2

def handler(event,context):
    headers = { 'Accept': 'application/json', 'User-Agent': 'https://github.com/acharrett/NoServerNovember/tree/master/Lorem' }
    request = urllib2.Request('http://www.randomtext.me/api/gibberish/', headers=headers)
    lorem_response = urllib2.urlopen(request).read()
    lorem_dict = json.loads(lorem_response)

    body_text = gen_html_body(lorem_dict['text_out'])
   
    response = {
        "statusCode": 200,
        "headers": {
           'Content-type': 'text/html',
           'Cache-Control': 'no-store, no-cache, must-revalidate',
        },
        "body": body_text,
    }

    return response 

def gen_html_body(message):
    body_text = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'
    body_text += '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">\n'
    body_text += '<head>\n'
    body_text += '<meta http-equiv="Content-Type" content="text/htmlcharset=utf-8" />\n'
    body_text += '<title>#noServerNovember</title></head>\n'
    body_text += '<body><h2><center><a href="https://serverless.com/blog/no-server-november-challenge/">#noServerNovember</a></center></h2>\n'
    body_text += message
    body_text += '<center><img src="https://cdn-images-1.medium.com/max/1600/1*f8e5opc7oUsKsUKbACDTrw.png"></center>\n'
    body_text += '</body></html>\n'


    return body_text

