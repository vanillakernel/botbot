#!/bin/python

# Slack integration for this bot.
import time 
from slackclient import SlackClient

# Load bot token
with open ('../botfly_token', 'r') as token_file  :
    token = token_file.readline().rstrip('\n') # readline() adds a newline, so we get rid of it.

sc = SlackClient(token)
print sc.api_call("api.test")
if sc.rtm_connect():
	while True:
	    stuff=sc.rtm_read()
	    for each in stuff:
		print stuff
	    time.sleep(1)
else:
    print "OH NOES"
