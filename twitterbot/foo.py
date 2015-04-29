from random import random
import requests
import json

def find_first_GiveMeAnime_tagged_mention(mentions):
    """
    Given a list of tweets (ostensibly from the mentions-API-endpoint),
    find the earliest one that has the #GiveMeAnime tag in it
    Arguments:
        mentions (list): a list of Twitter tweet objects that are dicts
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    animentions = []
    for m in animentions:
        hashtags = m['entities']['hashtags']
        for tag in hashtags:
            if tag['text'].upper() == "GIVEMEANIME":
                animentions.append(m)

    if len(animentions) > 0:
        return animentions[0]
    else:
        return None



def latest_Anime_reply(tweets):
    """
    Given a list of tweets (ostensibly from user_timeline API endpoint),
    find the earliest one that has the #ANIME4U hashtag in it
    Arguments:
        tweets (list): a list of Twitter tweet objects that are dicts
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """
    for tweet in tweets:
        tags = [tag for tag in tweet['entities']['hashtags'] if tag['text'].upper() == 'ANIME4U']
        if len(tags) > 0:
            return tweet


def anime_search():
   """
    Searches through the Hummingbird Database if a query term is given.
    Returns the best match anime if a result is found. 
    If nothing is found, return a random anime. 
    If no query term is given, also return a random anime. 

    Arguments:
        tweet (dict) of the tweet to reply to 
        
    Returns:
        A string to be tweeted containing the following: 
        1) the title of the resulting anime
        2) hummingbird url of the resulting anime
    """
    query = tweet['text']
    """
    Need to remove the @hummingbirdDB and #GiveMeAnime part at the front 

    """
    id_base_url = "http://hummingbird.me/api/v1/anime/"
    max_id = 10877
    random_anime_id = random.randrange(1, max_id, 1)

    if len(query) > 0:
        anime = requests.get("http://hummingbird.me/api/v1/search/anime", params={'query': query})    
        txt = anime.text
        data = json.loads(txt)
        if(len(data) > 0):
            title = data[random.randrange(0, len(data)-1, 1)]
            tweet_text = "#Anime4U How about \"" + title["title"] + "\"? " + title["url"]  
        else:
            anime_alt = requests.get(id_base_url + str(random_anime_id))
            txt = anime.text
            data = json.loads(txt)
            title = data[0]
            tweet_text = "#Anime4U How about \"" + title["title"] + "\"? " + title["url"]
    else:
        anime_alt = requests.get(id_base_url + str(random_anime_id))
        txt = anime.text
        data = json.loads(txt)
        title = data[0]
        tweet_text = "#Anime4U How about \"" + title["title"] + "\"? " + title["url"]

    return tweet_text