mixpanel-fake-data-gen
======================

Mixpanel Fake Data Generator
Mixpanel class definition found in beckiesmixpanel.py

This repo is designed to give you tools to make fake data in a Mixpanel project.
Version 1 populates a simple 3- step funnel where you can change the following params in the 'MakeConversionFunnel.py' script:

(Decimal) conversion rates between steps:
- PERCENT_STEP1_STEP2 = .85
- PERCENT_STEP2_STEP3 = .6

(String) event names:
- EVENT_NAME_1 = "Landing Page Loaded"
- EVENT_NAME_2 = "Signup Page Loaded"
- EVENT_NAME_3 = "Signup Complete"

(Integer) number of initial users you would like to be part of this funnel:
- INITIAL_USERS = 100

More flexibility to come!