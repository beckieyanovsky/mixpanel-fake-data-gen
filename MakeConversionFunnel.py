"""
#Simple script that creates a 3 step funnel with Z percent conversion rate where Z is user inputted (% Step 1 to 2 Conversion) * (% Step 2 to 3 Conversion)

# Variables you can manipulate:
# PERCENT_STEP1_STEP2
# PERCENT_STEP2_STEP3
# EVENT_NAME_1
# EVENT_NAME_2
# EVENT_NAME_3
# INITIAL_USERS
"""

#import libraries
import beckiesmixpanel
import credentials
import datetime
import json
import random
import time
from time import mktime



# Please enter a decimal for the percent conversion you'd like for each step. For example, .35 would indicate a 35% conversion rate
PERCENT_STEP1_STEP2 = .85
PERCENT_STEP2_STEP3 = .2
#OVERALL_CONVERSION = (PERCENT_STEP1_STEP2 * PERCENT_STEP2_STEP3)

#Please enter the names for the three events relevant to the funnel:
EVENT_NAME_1 = "Landing Page Loaded"
EVENT_NAME_2 = "Signup Page Loaded"
EVENT_NAME_3 = "Signup Complete"

#Please enter the number of initial users you would like to be part of this funnel. 
INITIAL_USERS = 1000

#UTC time
T = datetime.datetime(1970, 1, 1)



#This method takes in a distinct_id, a dictionary of {"event_name", {"property_name":property value}}, 
# a list of events, and a list of conversion floats and makes a funnel 
def move_user_through_conversion_funnel(self, distinct_id, events_dict, events_list, conversions, time_period):
	#check if valid value for time_period; else sets to minutes
	valid_times = ['minutes', 'days', 'weeks']
	if time_period not in valid_times:
		time_period = 'minutes'
	#check if number of conversion percentages is one less than number of events
	while (len(conversions)+1) != len(events_list):
		#if not enough conversion percentages given, append 0.0 to the list until there are enough
		if (len(conversions) < len(events_list)):
			conversions.append(0.0)
		#if too many conversion percentages given, remove last value until there are right amount
		elif ((len(conversions) >= (len(events_list)))):
			conversions.pop()
	#for every user, tracks the first event in the funnel
	start_time = int((datetime.datetime.utcfromtimestamp(self.now - random.randint(0, self.six_month))-T).total_seconds())
	#print start_time
	self.track(distinct_id, events_list[0], events_dict.get(events_list[0]), start_time)
	print distinct_id
	event_time = start_time
	iterator = 0
	while iterator <= (len(conversions)-1):
		r = random.random()
		if r < conversions[iterator]:
			interval_type = time_period
			interval_num = random.randint(1, 5)
			event_time += (datetime.timedelta(**{interval_type: interval_num})).total_seconds()
			self.track(distinct_id, events_list[(iterator+1)], events_dict.get(events_list[(iterator+1)]), event_time)
			print events_list[(iterator+1)]
		iterator += 1


if __name__ == '__main__':
	mp = beckiesmixpanel.Mixpanel(
		api_key = credentials.api_key,
		api_secret = credentials.api_secret,
		token = credentials.token
    	)
	distinct_id = 1
	super_properties = {}
	events = [EVENT_NAME_1, EVENT_NAME_2, EVENT_NAME_3]
	conversions = [PERCENT_STEP1_STEP2, PERCENT_STEP2_STEP3]
	while distinct_id <= INITIAL_USERS:
		#make dictionary of super properties
		gender = mp.assign_gender()
		gender_dict = {'Gender': gender}
		super_properties.update(gender_dict)
		#make dictionary of {events:{their properties}}
		event_prop_dict = {}
		for event in events:
			event_prop_dict[event]=super_properties
		#move a user through the funnel based on conversion rates provided above
		move_user_through_conversion_funnel(mp, distinct_id, event_prop_dict, events, conversions, "minutes")
		distinct_id += 1