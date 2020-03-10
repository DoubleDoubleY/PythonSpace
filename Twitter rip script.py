# Import libraries
from twython import Twython  
import json
import pandas as pd
import time


# REGISTER AN APP WITH TWITTER AND INSERT THE CONSUMER KEY AND CONSUMER SECRET HERE 
python_tweets = Twython(['07579865149'], ['888888'])


# list of terms to search for
terms = ['football', 'taylor swift', 'cats', 'wmgwarwick', 'avengers']

counter = 1

# Loop through the terms in the terms list
for term in terms:
	# Create our query. Specify 'recent' for most recent and 'popular' for most poplar. 'count' is the max number to extract. 'lang' is the # language
	query = {'q': term,  
	        'result_type': 'popular',
	        'count': 100,
	        'lang': 'en',
	        }

	# Search tweets
	# Specify data required
	dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
	# loop through the tweets and exrtract data  
	for status in python_tweets.search(**query)['statuses']:  
	    dict_['user'].append(status['user']['screen_name'])
	    dict_['date'].append(status['created_at'])
	    dict_['text'].append(status['text'])
	    dict_['favorite_count'].append(status['favorite_count'])

	# Structure data in a pandas DataFrame for easier manipulation. If its the first tweet then build a DataFrame from it. Otherwise, build # a second DataFrame and concatenate
	if counter == 1:
		df = pd.DataFrame(dict_)
	else:
		df2 = pd.DataFrame(dict_)
		df = pd.concat([df, df2])
	counter = counter + 1
	# print the number of rows
	print(len(df.index))
	# timeout for 15 minutes plus some change so not to throttle the app
	if counter != len(terms):
		time.sleep(950)

# Sort and export
df.sort_values(by='favorite_count', inplace=True, ascending=False)
# change to a local folder
df.to_csv('C:/Users/mmy/Desktop/outputFinal.csv')