import sys
import os
from twython import Twython

APP_KEY = ' '
APP_SECRET = ' '
OAUTH_TOKEN = ' '  # Access Token here
OAUTH_TOKEN_SECRET = ' '  # Access Token Secret here

api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

cmd = 'boinccmd --get_project_status | grep "user_total_credit"'
line = os.popen(cmd).readline().strip()
utc = line.split(': ')[1]
cmd = 'boinccmd --get_project_status | grep "user_expavg_credit"'
line = os.popen(cmd).readline().strip()
uavgc = line.split(': ')[1]
cmd = 'boinccmd --get_project_status | grep "host_total_credit"'
line = os.popen(cmd).readline().strip()
htc = line.split(': ')[1]
cmd = 'boinccmd --get_project_status | grep "host_expavg_credit"'
line = os.popen(cmd).readline().strip()
havgc = line.split(': ')[1]
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()

api.update_status(status='#EinsteinAtHome\nUTC '+utc+'\nUAvgC '+uavgc+'\nHTC '+htc+'\nHAvgC '+havgc+'\nCurrent CPU '+line+'\n#RaspberryPi #BOINC')

#print '#EinsteinAtHome\nUTC '+utc+'\nUAvgC '+uavgc+'\nHTC '+htc+'\nHAvgC '+havgc+'\nCurrent CPU '+line+'\n#RaspberryPi #BOINC'
