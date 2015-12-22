#!/bin/python2.7
# we use https://github.com/tweepy/tweepy by doing pip install tweepy
from __future__ import absolute_import, print_function
import tweepy
import json
from pprint import pprint
import argparse

def main ():
  parser = argparse.ArgumentParser()
  parser.add_argument("user", help="Twitter username")
  args=parser.parse_args()

  #read credentials from a file
  with open('../credentials.json') as data_file:    
    data = json.load(data_file)
    consumer_key=data["consumer_key"]
    consumer_secret=data["consumer_secret"]
    access_token=data["access_token"]
    access_token_secret=data["access_token_secret"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    user = args.user
    statuses=api.user_timeline(user)
    # If the authentication was successful, you should
    # see the name of the account print out
    print(api.me().name)
    for status in statuses:
      print(status.text)
   

  
if __name__ == "__main__":
  main()

