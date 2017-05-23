#Simple basic Twitter Streaming API with Filters
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#supply your Twitter keys here
consumer_key = '<--consumer_key-->'
consumer_secret = '<--consumer_secret -->'
access_token = '<--access_token-->'
access_token_secret = '<--access_token_secret-->'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        # write to a txt file
        with open('<--txt file directory-->','a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'trump'
    stream.filter(track=['trump'])
    #This line filter Twitter Streams to capture data by 'NYT', 'CNN'
    #stream.filter(follow=['807095', '759251'])