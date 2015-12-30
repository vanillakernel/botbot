#!/bin/python2.7
# we use https://github.com/tweepy/tweepy by doing pip install tweepy
from pprint import pprint
import argparse
import re
import random

def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="A sample file to markov chain.")
    args=parser.parse_args()
    f = args.file
    word_hash={}

    #read credentials from a file
    with open(f) as sample_file:    
      sample_text=sample_file.read()
  
    words = filter(None,( re.split('[-,.\"?! :\n\r]', sample_text)) ) 
  
    tuple_generator = Group(words)
    for group in tuple_generator:
      ToDict(group, word_hash)
#    pprint (word_hash)
    print ("Lines Scanned from %r : %r ") %  (f,len(sample_text))
    print ("Total hashes created: %r ") % (len(word_hash))
    print ("I MADE THIS FOR YOU I LOVE YOU: \n %r") % (MarkovPrivilege(word_hash, words))

# This will take the key array and make N-ples where the cohesion variable
# dictates how many words are in the key. 
def Group(word_array):
    if len(word_array) < 3: # TODO make this configurable.
	return						
    for i in range(len(word_array) - 2):
	yield (word_array[i], word_array[i+1], word_array[i+2])
	
#This will break the tuples in to a hash as "W1-W2":"W3"
def ToDict(tple, word_hash):
    k1, k2, w1 = tple
    k = (k1, k2)
    if k in word_hash:
	word_hash[k].append(w1)
    else:
        word_hash[k] = [w1]
    return

def MarkovPrivilege(word_hash, words):
    sentence_length = 25
    start = random.randint(0, len(words)-3)
    start, start_plus = words[start],words[start+1]
    w1, w2 = start, start_plus
    sentence = []
    for i in xrange(sentence_length):
	sentence.append(w1)
	w1, w2 = w2, random.choice(word_hash[(w1, w2)])
    sentence.append(w2)
    return ' '.join(sentence)


if __name__ == "__main__":
  main()
