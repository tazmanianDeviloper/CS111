# ps4pr3.py (Problem Set 4, Problem 3)        
#
# Problem 3: Recursive operations on binary numbers
#

#1
def bitwise_and(b1,b2):
    """If both binary strings are empty then an empty string is returned,
which is also our base case. During recursion, if one string depletes faster,
then the length of the remaining string is multiplyed by '0' and stored in the
stored_value. During call-backs each char from right to left is compared and
concatinated to stored_value."""
    if len(b1)==0 or len(b2)==0:
        if len(b1)>len(b2):
            return '0'*len(b1)
        elif len(b1)<len(b2):
            return '0'*len(b2)
        else:
            return ''
    else:
        stored_value=bitwise_and(b1[:-1],b2[:-1])
        if b1[-1]=='0' or b2[-1]=='0':
            return stored_value+'0'
        else:
            return stored_value+'1'

#2
def add_bitwise(b1, b2):
    """With recursion the length of both strings is reduced. If one reaches 0, then
the other one is returned and stored in the stored_value. Then the last index of both
string is checked. i one is 0 but the other is 1 then 1 is concatinated to stored_value,
but if both are 1 then one of them must be replaced by stored value and with the other be sent
back to the function call, where they are once again reduced so that one of them could become
an empty string again. Doing this means that one step will be added to recusrion."""
    if len(b1)==0 or len(b2)==0:
        if len(b1)>len(b2):
            return b1
        elif len(b1)<len(b2):
            return b2
        else:
            return ''
    else:
        stored_value=add_bitwise(b1[:-1],b2[:-1])
        if b1[-1]=='0' and b2[-1]=='0':
            return stored_value+'0'
        elif b1[-1]=='1' and b2[-1]=='0':
            return stored_value+'1'
        elif b1[-1]=='0' and b2[-1]=='1':
            return stored_value+'1'
        else:
            return add_bitwise(stored_value,'1')+'0'
    
        
        
        
