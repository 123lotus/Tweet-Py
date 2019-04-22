# Tweet-Py
This is an exercise i completed to scrub Twitter

I set up my own Twitter API's as signed up as a developer
Using these API keys i scrubbed twitter for Tweets on the Kardashians, Kanye West, Kendall and Kylie Jenner.  
In the sample code i of course deleted my API keys.

here are the results:

fetched_tweets = api.search(q=['kardashian','kanye','kendall jenner','kylie jenner'], result_type='recent', lang='en', count=100)
print("Number of tweets: {}".format(len(fetched_tweets)))

the above yielded the follwoing:  Number of tweets: 5

for tweet in fetched_tweets:
  print('Tweet ID: {}, Tweet Text: {}\n'.format(tweet.id, tweet.text))
  
  The above yielded the following:
  Tweet ID: 1120279363642118144, Tweet Text: @KimKardashian @kourtneykardash
@kanyewest  @usweekly

WHO THE HELL CARES?

How Kim, Kourtney and Khloe Kardashian,… https://t.co/XaMmL7tRbS

Tweet ID: 1120255941918830592, Tweet Text: Kanye’s wife Kim Kardashian led the pack, with Kris Jenner, Kendall, Kylie, Kourtney and Khloe all pictured watchin… https://t.co/vLjFTXgzra

Tweet ID: 1120083069854261251, Tweet Text: How Kim, Kourtney and Khloe Kardashian, Kendall and Kylie Jenner Celebrated Easter at Coachella: Photos - Us Weekly https://t.co/OuobiLw2ZZ

Tweet ID: 1120075391232688128, Tweet Text: How the Kardashians Celebrated Easter at Coachella: Pics
https://t.co/erkPIf7dgi

Kim, Kourtney and Khloé Kardashia… https://t.co/cztir7LQxe

Tweet ID: 1117714292982206464, Tweet Text: @YeezusMde I don’t hate; and feel sorry for what happened to all of Kris and Rob / Kardashian and Jenner offspring.… https://t.co/QfROBbsfSG
