# Beckie's first Python script that sends an event to her test project using the Mixpanel class created in beckiesmixpanel.py


#set of funnels that convert 
#retention rates
#^both of the above varying for different TYPES of users (type is as you define)

#import libraries
import beckiesmixpanel
import credentials

if __name__ == '__main__':
	mixpanel = beckiesmixpanel.Mixpanel(
		api_key = credentials.api_key,
		api_secret = credentials.api_secret,
		token = credentials.token
        )
	properties = {}
	for user in range (0,2):
		event = "event" + str(user)
		for letter in "Test":
			properties.update({"random_property_"+letter : letter})
			mixpanel.track(user, event, properties)