"""
#Simple script that creates a 3 step funnel with Z percent conversion rate where Z is user inputted (% Step 1 to 2 Conversion) * (% Step 2 to 3 Conversion)

# Variables you can manipulate:
# PERCENT_STEP1_STEP2
# PERCENT_STEP2_STEP3
# EVENT_NAME_1
# EVENT_NAME_2
# EVENT_NAME_3
# INITIAL_USERS

#import libraries
"""
import beckiesmixpanel
import credentials
import random


# Please enter a decimal for the percent conversion you'd like for each step. For example, .35 would indicate a 35% conversion rate
PERCENT_STEP1_STEP2 = .85
PERCENT_STEP2_STEP3 = .6
#OVERALL_CONVERSION = (PERCENT_STEP1_STEP2 * PERCENT_STEP2_STEP3)

#Please enter the names for the three events relevant to the funnel:
EVENT_NAME_1 = "Landing Page Loaded"
EVENT_NAME_2 = "Signup Page Loaded"
EVENT_NAME_3 = "Signup Complete"

#Please enter the number of initial users you would like to be part of this funnel. 
INITIAL_USERS = 10


#This method randomly assigns a "Male" or "Female" value with assigned frequency
def assign_gender():
	gender = random.choice(['Female', 'Male'])
	print gender
	return gender

#This method takes in a dictionary of {"event_name", {"property_name":property value}}, 
# and a list of conversion floats and makes a funnel 
def move_user_through_conversion_funnel(distinct_id, events_dict, events_list, conversions):
	#check if number of conversion percentages is one less than number of events
	while (len(conversions)+1) != len(events):
		#if not enough conversion percentages given, append 0.0 to the list until there are enough
		if (len(conversions) < len(events)):
			conversions.append(0.0)
		#if too many conversion percentages given, remove last value until there are right amount
		elif ((len(conversions) >= (len(events)))):
			conversions.pop()
	#for every user, tracks the first event in the funnel
	mp.track(distinct_id, events_list[0], events_dict.get(events_list[0]))
	iterator = 0
	while iterator <= (len(conversions)-1):
		r = random.random()
		if r < conversions[iterator]:
			mp.track(distinct_id, events_list[(iterator+1)], events_dict.get(events_list[(iterator+1)]))
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
		gender = assign_gender()
		gender_dict = {'Gender': gender}
		super_properties.update(gender_dict)
		#make dictionary of {events:{their properties}}
		event_prop_dict = {}
		for event in events:
			event_prop_dict[event]=super_properties
		#move a user through the funnel based on conversion rates provided above
		move_user_through_conversion_funnel(distinct_id, event_prop_dict, events, conversions)
		distinct_id += 1



