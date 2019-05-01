#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price_so_far = None
  max_profit_so_far = None # current_min_price_so_far - current_highest_price_so_far
  current_highest_price_so_far = None
  # go through the list and find the smallest price
  # use the smallest price to find the difference between it and the largests price so far to get the max profit so far
  # Largest price should be before the smallest price, smallest can't come after the largest price
  for i in range(len(prices)):
    current_price = prices[i]
    if current_min_price_so_far:
      if current_highest_price_so_far:
        if current_price > current_highest_price_so_far:
          current_highest_price_so_far = current_price
          if prices[i-1] < current_min_price_so_far:
            current_min_price_so_far = prices[i-1]
        else:
          max_profit_so_far = current_highest_price_so_far - current_min_price_so_far
      else:
        current_highest_price_so_far = current_price
    else:
      current_min_price_so_far = current_price 
  
  return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))