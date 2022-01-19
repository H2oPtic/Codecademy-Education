def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Write code here

def calculate_simple_return(start_price, end_price, dividend = 0):
  return  (end_price - start_price + dividend) / start_price

simple_return = calculate_simple_return(200, 250)

print('The simple rate of return is ' + display_as_percentage(simple_return))



#EQUATION:
#R=(E - S + D) / S


    #R: simple rate of return
    #S: starting price of investment
    #E: ending price of investment
    #D: dividend

