# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design

# 1. Using LC, write a function that takes as input a list of numbers called values,
# and return a list containing the cubes of the numbers in values

def cube_all_lc(values):
    """using lc and list manipulation(inexing),
    x in each iteration has been raised to the power of 3"""
    lc_cube=[x**3 for x in values[0:]]
    return lc_cube

def cube_all_rec(values):
    """nothing raised to the power of 3 is still nothing,
    so len of nothing would be the base case. If the len is 1 then no recursion is needed,
    but beyond that in each itteration the values have to be concatinated."""
    if len(values)==0:
        return [0]
    else:
        stored_values=cube_all_rec(values[1:])
        if len(values)==1:
            return [values[0]**3]
        else:
            return [values[0]**3]+stored_values

def num_larger(threshold, values):
    """using recursion the elngth of values is reduced to 0, and stored in stored_value.
during the recursion, each the 0 index of values are checked against the threshold,
and the returned vaue is saved in the stored value"""
    if len(values)==0:
        return 0
    else:
        stored_value=num_larger(threshold, values[1:])
        if values[0]>threshold:
            return stored_value+1
        else:
            return stored_value+0

def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_consonants(words):
    """If there are no words in the list then there is nothing to count consonants for.
The base case, there for, shall be an empty string. Actual inputs will be reduced to 0,
on the first itteration in recursion the first input is saved as the stored_value. from
then, in every other itteration, the length of the first index is measured against the length
of the stored_value."""
    if len(words)==0:
        return ''
    else:
        stored_value=most_consonants(words[1:])
        if len(words)==1:
            stored_value=words[0]
            return stored_value
        else:
            if len(stored_value)-(num_vowels(stored_value))>=len(words[0])-(num_vowels(words[0])):
                return stored_value
            else:
                return words[0]

def price_string(cents):
    """using conditional statements and string concatinations"""
    d = cents//100         # compute whole number of dollars
    c = (cents*100)//100   # compute remaining cents

    price=str(cents)        # initial value of the price string

    if len(price)<=2:
        price=str(c)
        price=price +' cents'
        return price
    else:
        d=price[:-2]
        c=price[-2:]
        if price[-2:]=='00':
            price=d+' dollars, '
            return price
        elif price[-2]=='0':
            c=price[-1]
            price=d+' dollars, '+c+' cents'
            return price
        else:
            return d+' dollars, '+c+' cents'
            


        

           
    

            
                                        
                                        

        
    

            
            
    
