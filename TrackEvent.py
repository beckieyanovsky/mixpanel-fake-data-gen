# Beckie's first Python script that sends an event to her test project

#set of funnels that convert 
#retention rates
#^both of the above varying for different TYPES of users (type is as you define)

#import libraries
import base64
import json
import time
from urllib2 import urlopen
import urllib2
import urllib
import credentials

ENDPOINT = 'https://api.mixpanel.com/track'


class Mixpanel(object):
	def __init__(self, api_key, api_secret, token):
		self.api_key = api_key
		self.api_secret = api_secret
		self.token = token

	def track(self, distinct_id, event_name, added_properties={}):
		"""
		Pass this method a Mixpanel object, distinct_id, event_name, and hash table of properties 
		and it will track that event in the mixpanel project with same credentials as Mixpanel object
		that called it.
		"""

		properties = {
			'distinct_id' : distinct_id,
			'time' : int(time.time()),
			'token' : mp.token
		}
		properties.update(added_properties)
		event = {
			'event' : event_name,
			'properties' : properties
		}
		event_json = json.dumps(event, separators=(',', ':'))
		data = {
			'data':base64.b64encode(event_json),
			'verbose':1,
			'ip':0,
			'api_key': mp.api_key
		}


		encoded_data = urllib.urlencode(data)
		print encoded_data
		request = urllib2.Request(ENDPOINT, encoded_data)

		response = urllib2.urlopen(request).read()
		print response

if __name__ == '__main__':
	mp = Mixpanel(
		api_key = credentials.api_key,
		api_secret = credentials.api_secret,
		token = credentials.token
        )
	properties = {}
	for user in range (0,2):
		event = "event" + str(user)
		for letter in "Test":
			properties.update({"random_property_"+letter : letter})
			mp.track(user, event, properties)
