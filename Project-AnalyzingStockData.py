from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# Write code here

def get_returns(prices):
  returns = []
  for i in prices:
    rate_of_return = calculate_log_return(i, i + 1)
    returns.append(rate_of_return)
  return returns

amazon_returns = get_returns(amazon_prices) 
ebay_returns = get_returns(ebay_prices)

print(amazon_returns)
print(ebay_returns)
