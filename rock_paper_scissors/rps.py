#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # create a list that will hold all the possible cominations
  # for however many combinations there are add the possible cominations to the list with out repeats
  # create a starting list with the options of rock paper and scissors
  # loop throug the length of the rps list and hold the starting option in a value
  # do another loop that does a recusive call which gets the possible combinations from that starting value
  rps = ['rock', 'paper', 'scissors']
  res=[]
  if n==0:
      return [[]]
  else:
    for i in range(0,len(rps)):
      start=rps[i]
      for combo in rock_paper_scissors(n-1):
          res.append([start]+combo)

    return res

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')