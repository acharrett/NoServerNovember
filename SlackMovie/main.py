import json
import os
import random
import urllib2

def handler(event,context):
    movie = get_movie()

    reply_text = movie['original_title']

    result = {}
    result['response_type'] = 'in_channel'
    result['text'] = "Try this movie!"
    result['attachments'] = [ { "text": reply_text }, { "image_url": movie['full_poster_url'] } ]
    result_json = json.dumps(result)

    response = {
        "statusCode": 200,
        "headers": {
           'Content-type': 'application/json',
        },
        "body": result_json,
    }

    return response

def get_movie():
    request_url = 'https://api.themoviedb.org/3/discover/movie?api_key='
    request_url += os.environ['MOVIE_API_KEY']
    request_url += '&primary_release_date.gte=1980-01-01'
    request_url += '&primary_release_date.lte=1989-12-21'
    request_url += '&with_genre=28'

    headers = { 'Accept': 'application/json', 'User-Agent': 'https://github.com/acharrett/NoServerNovember/tree/master/SlackMovie' }
    movie_request = urllib2.Request(request_url, headers=headers)
    movie_response = urllib2.urlopen(movie_request).read()
    movies = json.loads(movie_response)

    results_num = len(movies['results'])
    results_num -= 1

    found_movie = movies['results'][random.randint(0,results_num)]
    found_movie['full_poster_url'] = 'http://image.tmdb.org/t/p/w185' + found_movie['poster_path']

    return found_movie
