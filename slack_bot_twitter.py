#!/bin/python

# Slack integration for this bot.
import time
import json
import markov
from slackclient import SlackClient
import twitter_seed as ts
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("user", help="Twitter username")
parser.add_argument("count", help="Number of statuses to return")
args=parser.parse_args()
user = args.user
count = args.count
api = ts.authenticate()
statuses = ts.get_statuses(api, user, count)
ts.print_statuses(user,statuses)

# Load bot token
with open ('../botfly_token', 'r') as token_file  :
    token = token_file.readline().rstrip('\n') # readline() adds a newline, so we get rid of it.

sc = SlackClient(token)
#print sc.api_call("api.test")
if sc.rtm_connect():
	botname=sc.server.username #this is set in the server class of slackclient lib
	while True:
	    stuff=sc.rtm_read()
            for index, event in enumerate(stuff): 
              if 'type' not in event:
                continue 
              if event['type'] == "message":
                if str.lower(str(event['text'])).find(str.lower(str(botname))) != -1:
                  message = markov.markov()
                  sc.rtm_send_message(event['channel'], message)
	    time.sleep(1)
else:
    print "OH NOES"


'''

[{u'text': u'That is better', u'ts': u'1451505175.000109', u'user': u'U0HA6RM34', u'team': u'T0CP5S4RH', u'type': u'message', u'channel': u'C0CPC37AM'}]

'''
