# THIS FILE CONTAINS THE MIXPANEL CLASS DEFINITION, INCLUDING THE FOLLOWING FUNCTIONS:
# -track

import base64
import credentials
import datetime
import json
import random
import time
from urllib2 import urlopen
import urllib2
import urllib

ENDPOINT = 'https://api.mixpanel.com/import'


class Mixpanel(object):
	def __init__(self, api_key, api_secret, token):
		self.api_key = api_key
		self.api_secret = api_secret
		self.token = token

	#time variables
	now = int(time.time())
	one_day = datetime.timedelta(days=1).total_seconds()
	seven_days = datetime.timedelta(days=7).total_seconds()
	one_month = datetime.timedelta(weeks=4).total_seconds()
	six_month = datetime.timedelta(weeks=24).total_seconds()

	#This method randomly assigns a gender value 
	def assign_gender(self):
		gender = random.choice(['Female', 'Male', 'Unknown'])
		return gender

	#This method randomly assigns an OS value 
	def assign_os(self):
		os = random.choice(['Linux', 'Unix', 'Windows', 'OSX', 'iOS','Android'])
		return os

	def track(self, distinct_id, event_name, added_properties={}, time = int(time.time())):
		"""
		Pass this method a Mixpanel object, distinct_id, event_name, and hash table of properties 
		and it will track that event in the mixpanel project with same credentials as Mixpanel object
		that called it.
		"""
		properties = {
			'distinct_id' : distinct_id,
			'time' : time,
			'token' : self.token
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
			'api_key': self.api_key
		}


		encoded_data = urllib.urlencode(data)
		#print encoded_data
		request = urllib2.Request(ENDPOINT, encoded_data)
		print request

		response = urllib2.urlopen(request).read()
		print response
