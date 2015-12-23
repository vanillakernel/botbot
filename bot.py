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
      sample_text=sample_file.read()
  
    words = filter(None,( re.split('[-,.\"?! :\n]', sample_text)) ) 
  
    triple_generator = Group(words)
    for triple in triple_generator:
      print(triple)
   

# This will take the word array and make N-ples where the cohesion variable
# dictates how many words are in the key. 
def Group(word_array):
    if len(word_array) < 3:
	return						
    for i in range(len(word_array) - 2):
	yield (word_array[i], word_array[i+1], word_array[i+2])
	
#This will map the N-ples as "W1-Wn":"Wlast"
def ToDict(tuple_array):
  return
  
if __name__ == "__main__":
  main()

