# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#


# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

def first_and_last(values):
    """seperating the first and the last values of a set using indexting"""
    first=values[0]
    last=values[-1]
    return [first, last]

def longer_len(s1, s2):
    """Comparing the length of both inputs"""
    if len(s1) > len(s2):
        longer_len =len(s1)
    else:
         longer_len=len(s2)
    return longer_len

def move_to_end(s, n):
    """Using slicing, the function assigns n to the end indext,
then reassigns it to the first indext. Each time, the resulting substring is saved in a new
vaiable. The return call produces the concatination of values stoed in those variables."""
    a=s[0:n]
    b=s[n:]
    return b+a

    
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))
    

    # optional but encouraged: add test calls for your functions below
    print('If [1,20,30] is given as the values, then the method will print: ', first_and_last([1,20,30]))
    print('the longer length between "tay" and "taym" is "taym" which has a length of :', longer_len("tay", "taym"))
    print('the seperated substring indext value (2) of taymaz has been added to the end of it: ', move_to_end("taymaz", 2)) 
