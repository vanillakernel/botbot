#!/bin/python2.7
# we use https://github.com/tweepy/tweepy by doing pip install tweepy
import tweepy
import json
import argparse

def print_statuses(user,statuses):
  printable = []
  for status in statuses:
    print ("\n\n*" + user + ":* ")
    printable.append("\n\n*" + user + ":* ")
    print(status.text)
    printable.append(status.text)
  return printable

def get_statuses(api,user,count):
  statuses=api.user_timeline(user, count=count)
  return statuses 

#
# Uses a JSON cred file to access the twitter API
# Returns an API object.
#
def authenticate(): 
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
  if not api.verify_credentials(): #<-this call eturns false if auth fails.
    return False
  return api
    

def main ():
  parser = argparse.ArgumentParser()
  parser.add_argument("user", help="Twitter username")
  parser.add_argument("count", help="Number of statuses to return")
  args=parser.parse_args()
  user = args.user
  count = args.count
  api = authenticate()
  statuses = get_statuses(api, user, count)
  print_statuses(user,statuses)
  
if __name__ == "__main__":
  main()

