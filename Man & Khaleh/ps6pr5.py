#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Calculates the average price')
    print('(4) Calculates the standard deviation of prices')
    print('(5) Informs you of day of Max price')
    print('(6) Verifies if there are any prices below the threshold')
    print('(7) Best buying and selling dates, with Max profit')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
#1 Add support for option 3: finding the average price
def avg_price(prices):
    """using for loop the avareg of prices are calculated and returned"""
    average=0
    if len(prices)==0:
        print('No prices have been entered.')      
    elif len(prices)==1:
        print('The average of one entry is itself',prices[0], end=' ')        
    else:
        for i in range(len(prices)):
            average+=prices[i]
    return average/len(prices)

#2 Add support for option 4: finding the standard deviation
def std_dev(prices):
    """First the median of the prices is calculated, using
avg_price(prices)function. Then for every price in the prices[],
the price is subtracted from median, raised to the power of 2,
stored in itself, then cumilated in an instant variable. Ultimately
that instant variable, which holds the cumulative value of all
instances is devided by the length of [prices], and square rooted"""
    median=0
    iv=0
    if len(prices)==0:
        print('No prices have been entered.')      
    elif len(prices)==1:
        print('The standard diviation of one entry is itself',prices[0], end=' ')        
    else:
        median=avg_price(prices)
        for i in range(len(prices)):
            prices[i]=(prices[i]-median)**2
            iv+=prices[i]   
    return math.sqrt(iv/len(prices))

#3 Add support for option 5: finding the maximum price and its day
"""two variables have been initialized to carry the instant values
of for loop itterations. In each itteration the instant variables is
checked against those variables to figure out the max value"""
def max_day(prices):
    max_value=0
    max_value_index=0

    if len(prices)==0:
        print('No prices have been entered.')             
    else:
        for i in range(len(prices)):
            if prices[i]>max_value:
                max_value=prices[i]
                max_value_index=i
 
    return max_value_index

#4 Add support for option 6: testing a threshold
def any_below(prices, threshold):
    """Two variables are initialized to help lopp itterations. Once one index is found that is lower
that threshold, then the function returns True"""
    t=0
    f=0
    if int(threshold)<=0:
        print('Threshold can not be 0')
    else:
        for price in prices:
            if price<int(threshold):
                t+=1
            else:
                f+=1
        if t>=1:
            return True
        else:
            return False

#5 Add support for option 7: the “time travel” investment strategy discussed in lecture
def find_plan(prices):
    """Sice buying has to occure before selling it the days must
be divided in to two groups. The middle index woud be the devider.
the lowest perice is set at zero index where as the highest price
is set as the middle index. the remaining prices are compared to
these two. if the a lower price is found the lp will be assigned
to that price, and so will be the case with hp"""
    middle=len(prices)//2
    lp=prices[0]
    lp_index=0
    hp=prices[middle]
    hp_index=middle  
    if len(prices)<2:
        print('For comparison at least 2 prices are needed')             
    else:
        for i in range(len(prices[:middle])):
            if prices[i]<lp:
                lp=prices[i]
                lp_index=i
        for index in range(middle,len(prices[middle:])):
            for instant_variable in prices[middle:]:
                if instant_variable>hp:
                    hp=instant_variable
                    index+=1
                    hp_index=index
        p_diff=hp-lp
        return [lp_index, hp_index, p_diff]                       

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average=avg_price(prices)
            print('The average of the prices enterd is: ',average)
        elif choice ==4:
            standard_dev=std_dev(prices)
            print('The standard diviation of your prices is: ',standard_dev)
        elif choice == 5:
            maximum=max_day(prices)
            print('The max price is on day:', maximum)
        elif choice == 6:
            threshold=input('Enter the threshold: ')
            boolean_value=any_below(prices, threshold)
            if boolean_value==True:
                print('There is at least one price below', threshold)
            else:
                print('There isn not any price below the threshold')
        elif choice == 7:
            buy_sell_max=find_plan(prices)
            print('best day to buy, sell, and Max profit', buy_sell_max)
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
