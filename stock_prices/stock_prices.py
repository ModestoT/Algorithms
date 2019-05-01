#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price_so_far = None
  max_profit_so_far = None # current_min_price_so_far - current price
  # go through the list and find the smallest price
  # use the smallest price to find the difference between it and the largests price so far to get the max profit so far
  # Largest price should be after the smallest price
  for i in range(len(prices)):
    current_price = prices[i]
    if current_min_price_so_far:
      if current_price > current_min_price_so_far:
        max_profit_so_far = current_price - current_min_price_so_far
      else:
        current_min_price_so_far = current_price
    else:
      current_min_price_so_far = current_price
  
  return max_profit_so_far

print(find_max_profit([10, 7, 5, 8, 11, 9]))
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))