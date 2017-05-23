Simple Basic Tweepy for Streaming API
================
The Twitter Streaming API is designed to deliver limited volumes of data via two main types of realtime data streams: sampled streams and filtered streams. Many users like to use the Streaming API because the streaming nature of the data delivery means that the data is delivered closer to realtime than it is from the Search API. But the Streaming API wasn’t designed to deliver full coverage results and so has some key limitations for enterprise customers. 

Filtered streams deliver all the Tweets that match a filter you select (eg. keywords, usernames, or geographical boundaries). This can be very useful for developers or businesses that need limited access to specific Tweets.

Filtered streams can be collected using Tweepy streaming functionallity. Tweepy needs users to set up "filter" (and it is a requirement). For example, this python application will listen to all mentions of "trump" on twitter or all streaming tweets from CNN and the New York Times.

Getting started:
* 1. Create a twitter app on twitter.com/dev
* 2. Install tweepy
* 3. Edit streaming.py with your application's Details https://dev.twitter.com/apps (under "OAuth settings")
* 4. Define your filters
* 5. Run "python streaming.py" using Terminal or Jupyter 

Enjoy!
