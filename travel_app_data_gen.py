"""
This script generates a *little bit* of fake data for a standard travel app.
Goals are to show: 
- A funnel where most users Book Flights, and fewer book Lodgin, and Rent cars
-
-
"""

#import libraries
import beckiesmixpanel
import credentials 
from MakeConversionFunnel import move_user_through_conversion_funnel

TOTAL_DISTINCT_IDS = 100


def set_super_properties(distinct_id):
	gender = mp.assign_gender()
	os = mp.assign_os()
	#set super properties 
	super_properties = {
		'Gender' : gender,
		'OS' : os,
		'distinct_id' : distinct_id
	}
	return super_properties

if __name__ == "__main__":
	mp = beckiesmixpanel.Mixpanel(
		api_key = credentials.api_key,
		api_secret = credentials.api_secret,
		token = credentials.token
		)
	event_list = ['Booked Flight', 'Booked Lodging', 'Booked Rental Car']
	conversions = [.85, .35]
	for user in range (0,TOTAL_DISTINCT_IDS):
		super_properties = set_super_properties(user)
		event_prop_dict = {}
		for event in event_list:
			event_prop_dict[event] = super_properties
		move_user_through_conversion_funnel(mp, user, event_prop_dict, event_list, conversions)