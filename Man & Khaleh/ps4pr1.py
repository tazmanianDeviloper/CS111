# ps4pr1.py (Problem Set 4, Problem 1)        
#
# Problem 1: From binary to decimal and back!
#

#1
def dec_to_bin(n):
    """If the entry is 0 no calculation is needed, if it is 1
then we will return the str of the remainder of the division in
which 1 has been devided by 2. Else we will devide n by 2 each time
to reduce n to smaller integers until we reach our base cases."""
    if n==0:
        return '0'
    elif n==1:
        return '1'   
    else:
        stored_value=dec_to_bin(n//2)
        if n%2==0:
            return stored_value+'0'
        else:
            return stored_value+'1'

#2
def bin_to_dec(b):
    """The first number from right is always itself, so that
must be one of our case cases. Every other number the right of
the first number, if it is 0, won't afect our algorithm, but if
it is a 1 then it has to be multiplied by 2, and that 2 must be
powered to the index of that 1"""
    if len(b)==1:
        return int(b)   
    else:
        stored_value=bin_to_dec(b[1:])
        if b[0]=='0':
            return stored_value
        else:
            return (int(b[0])*2)**int(len(b)-1) + stored_value       
    
