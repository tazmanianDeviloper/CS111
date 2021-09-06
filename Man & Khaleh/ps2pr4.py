
# 
# ps2pr4.py - Problem Set 2, Problem 4
#
#In this problem you will write three functions that employ the power of recursion!
#

#1
"""first n is reduced to 0,
at the base case the empty string is stored in stored_valu.
the stored value is concatinated to s and returned back to stored_value."""
def copy(s, n):
    if n<=0: 
        return '' 
    else:
        stored_value=copy(s, n-1)
        return s+stored_value
#2
def compare(list1, list2):
    """if both lists are empty compring them would be easier, thus the base case.
if the length of list1 is bigger than the length of list2, then list one indices must
must be compared to indices of list2 up to the limit of list2; or vice-versa."""
    if list1==list2:
        return 0
    else:
        stored_value=compare(list1[1:], list2[1:])
        if len(list1)>len(list2):  
            if list1[0:len(list2)]>=list2:
                return stored_value+0
            else:
                return stored_value+1
        elif len(list1)<len(list2):  
            if list1>=list2[0:len(list1)]:
                return stored_value+0
            else:
                return stored_value+1
        else:
            if list1>=list2:
                return stored_value+0
            else:
                return stored_value+1
#3
def double(s):
    """conditions are set to handle each case. In case of s being
of length 1 the base condition has been initialized. more than 1 in lenghth
will be recursed and concatinated to the base condition"""
    if len(s)==0:
        return ''
    else:
        stored_value=double(s[1:])
        if len(s)==1:
            return s[0]+s[0]
        else:
            return (s[0]+s[0])+stored_value

    
    
        

    
    















    
