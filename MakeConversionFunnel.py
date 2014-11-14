#Simple script that creates a 3 step funnel with Z percent conversion rate where Z is user inputted (% Step 1 to 2 Conversion) * (% Step 2 to 3 Conversion)

# Variables you can manipulate:
# PERCENT_STEP1_STEP2
# PERCENT_STEP2_STEP3
# EVENT_NAME_1
# EVENT_NAME_2
# EVENT_NAME_3
# INITIAL_USERS

#import libraries
import beckiesmixpanel
import random
import credentials


# Please enter a decimal for the percent conversion you'd like for each step. For example, .35 would indicate a 35% conversion rate
PERCENT_STEP1_STEP2 = .85
PERCENT_STEP2_STEP3 = .6
OVERALL_CONVERSION = (PERCENT_STEP1_STEP2 * PERCENT_STEP2_STEP3)

#Please enter the names for the three events relevant to the funnel:
EVENT_NAME_1 = "Landing Page Loaded"
EVENT_NAME_2 = "Signup Page Loaded"
EVENT_NAME_3 = "Signup Complete"

#Please enter the number of initial users you would like to be part of this funnel. 
INITIAL_USERS = 100



if __name__ == '__main__':
	mp = beckiesmixpanel.Mixpanel(
		api_key = credentials.api_key,
		api_secret = credentials.api_secret,
		token = credentials.token
    	)
	distinct_id = 1
	while distinct_id < INITIAL_USERS:
		mp.track(distinct_id, EVENT_NAME_1)
		randomFirstConversion = random.random()
		if randomFirstConversion < PERCENT_STEP1_STEP2:
			mp.track(distinct_id, EVENT_NAME_2)
			randomSecondConversion = random.random()
			if randomSecondConversion < PERCENT_STEP2_STEP3:
				mp.track(distinct_id, EVENT_NAME_3)
		distinct_id += 1



