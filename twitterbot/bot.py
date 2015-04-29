import foo
import twit_utils
CREDS_FILE = "~/Desktop/tw.json"

def make_it_so():
    # Step 1. Get my latest tweets
    tweets = twit_utils.get_latest_tweets_from_me(CREDS_FILE)
    print("Found", len(tweets), "tweets")

    # Step 2. From my tweets, get the last time I did a #Anime4U reply
    breply = foo.latest_Anime_reply(tweets)
    if breply:
        xid = breply['in_reply_to_status_id']
    else:
        xid = 1
    print("Searching for mentions with an id later than", xid)

    # Step 3. Get the most recent mentions since my last #Anime4U reply
    mentions = twit_utils.get_mentions(CREDS_FILE, {"since_id": xid})
    print("Found", len(mentions), "mentions")

    # Step 4. from the mentions, see if anyone has used the hashtag #GiveMeAnime
    animetweet = foo.find_first_GiveMeAnime_tagged_mention(mentions)

    if animetweet == None:
        print("No #GiveMeAnime tweet to reply to")
        return None
    else:
        # Step 5. Create the custom bro message
        print("About to send a message to", animetweet['user']['screen_name'])
        txt = foo.anime_search()

        # Step 6. Send the message
        resp = twit_utils.reply(CREDS_FILE, txt, animetweet)
        return resp



import time
print('round')
while True:
    make_it_so()
    time.sleep(10)