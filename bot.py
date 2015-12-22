#!/bin/python2.7
# we use https://github.com/tweepy/tweepy by doing pip install tweepy
from pprint import pprint
import argparse
import re
def main ():
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="A sample file to markov chain.")
  args=parser.parse_args()
  file = args.file
  cohesion=2 # Number of words to match for keys.
  
  #read credentials from a file
  with open('sample.txt') as sample_file:    

    # If the authentication was successful, you should
    # see the name of the account print out
    sample_text=sample_file.read()
    #word_dict=dict(x.split(' ') for x in sample_text.split('\n'))
    delimiters = ['\n', ' ', ',', '.', '?', '!', ':', 'and_what_else_you_need']
    words = filter(None,( re.split('[-,.\"?! :\n]', sample_text)) ) 
    pprint(words);
   

def Group(word_array):
  return
  # This will take the word array and make N-ples where the cohesion variable
  # dictates how many words are in the key. 

def ToDict(tuple_array):
  return
  #this will map the N-ples as "W1-Wn":"Wlast"
  



if __name__ == "__main__":
  main()

