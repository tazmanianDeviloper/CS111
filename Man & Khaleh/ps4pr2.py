# ps4pr2.py (Problem Set 4, Problem 2)        
#
# Problem 1: From binary to decimal and back!
#

# Problem 2: Using your conversion functions

from ps4pr1 import *

#1
def add(b1, b2):
    """Fallowing the instructions in blackboard, I passed the variables
to the functions in ps4pr1 and accumilated the resultas and passed that
result back to dec_to_bin() to get the output back in binary"""
    n1=bin_to_dec(b1)
    n2=bin_to_dec(b2)
    bsum=dec_to_bin(n1+n2)
    return bsum

#2
def increment(b):
    """figuring out the lenght of input in bin, converting binary input to decimal,
incrementing and converting back to binary, setting conditions to limit the output to 8 bits"""
    len_b=len(b)
    b_dec=bin_to_dec(b)
    incremented_b=dec_to_bin(b_dec+1)
    if len(incremented_b)>len_b:
        return incremented_b[1:]
    elif len(incremented_b)<len_b:
        len_dif=len_b-len(incremented_b)
        return(len_dif*'0')+incremented_b
    else:
        return incremented_b
        
    
 
    
