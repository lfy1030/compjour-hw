# Pitch

Anyone who tweets at my bot with the hashtag #discoverAnime with a query term will be tweeted back with the title of the anime that best matches the search term in the Hummingbird Database, a cover picture for the anime and the Hummingbird link to the anime.

In the event that the search term returned no results, a completely randomly selected anime will be tweeted. In the event that there is no query term behind the hashtag, a randomly selected anime will also be tweeted back. 

e.g. @discoverAnimeBot #searchAnime [query]
response: @user [COVER PICTURE] How about [Title]? https://hummingbird.me/anime/[best-match-slug]

# The Steps
1. Bot checks Twitter API endpoint of statuses/mentiones timeline
2. For each Tweet, the bot checks to see if the #discoverAnime hashtag was used. If the hashtag was used, the bot also checks if there are words behind. Any text that occurs behind the #discoverAnime hashtag will be considered the query text. 
3. The user's screenname and ID of the tag is also recorded. 
4. Using the [Hummingbid API V1](https://github.com/hummingbird-me/hummingbird/wiki/API-v1-Methods#anime--search-by-title), search for the anime with the given query term.
	..*If there was no query term
	..*If there were no search results
	..*Use a random number generator to generate a random number as the ID of the title to return

Otherwise get the top result of the query results and GET its title and the cover image. 

5. Construct the tweet and tweet back using the POST upload/media and POST statuses/update