"""
Simple script that builds retention data 

"""

#import libraries
import beckiesmixpanel
import credentials
import datetime
import time


#Please enter the names for event you'd like to make retention data for
EVENT_NAME_1 = "Landing Page Loaded"

#time variables
one_day = datetime.timedetla(days=1).total_seconds()
seven_days = datetime.timedelta(days=7).total_seconds()
one_month = datetime.timedelta(weeks=4).total_seconds()
six_month = datetime.timedelta(weeks=24).total_seconds()

now = int(time.time())





start = datetime.datetime.utcfromtimestamp(self.now - random.randint(0, self.half_year))


start += datetime.timedelta(seconds=random.randint(1, self.ten_days))
