#!/usr/bin/python

import sys

def making_change(amount, denominations):
  res = [0] * amount
  if amount == 0:
    print(amount, denominations)
    return 1
  elif amount < 0 or denominations == []:
    return 0
  else:
    # for coin in denominations:
    #   print('coin',coin)
    #   for higher_amount in range(coin, amount+1):
    #     print('amount',higher_amount)
    #     res[higher_amount-1] = higher_amount - coin
    # return res
    # return  making_change((amount- 50), denominations) + making_change((amount- 25), denominations) + making_change((amount- 10), denominations) + making_change((amount- 5), denominations) + making_change((amount- 1), denominations) 
    return  making_change(amount, denominations[:-1]) + making_change((amount - denominations[-1]), denominations) 
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")