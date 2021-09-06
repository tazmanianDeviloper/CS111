
# 
# ps3pr4.py - Problem Set 3, Problem 4
#
# This problem asks you to write three additional functions using the functional-programming techniques that we have discussed in lecture.
#

#1
"""If the list is empty -1 is returen. If the list is not empty
but starts with the elem then zero is returned. If the list doesn't
start with the elem then recursion starts. In each iteration, the first
value is checked against the base cases. If the 2nd case is met,
0 is stored in stored_value and in the reverse 0 is increased by 1
in each recall. If the second base case never happens the the first
one will eventually happen, in which case -1 is stored, which means
there were no elems in list. A Condition has been set to account for that
eventuality"""
def index(elem, seq):
    if len(seq)==0:
        return -1
    elif seq[0]==elem:
        return 0
    else:
        stored_value=index(elem, seq[1:])
        if stored_value==-1:
            return -1
        else:
            return stored_value+1
        
#2
def index_last(elem, seq):
    """Similar to the previous problem but the recursion starts
from last index which is -1, and the index count begins from the last
index so during re-call in each itteration the length of array is already
reduced by 1 index and stored in the stored_value, thus we just need to
return the stored_value"""
    if len(seq)==0:
        return -1
    elif seq[-1]==elem:
        return len(seq)-1
    else:
        stored_value=index_last(elem, seq[:-1])
        if stored_value==-1:
            return -1
        else:
            return stored_value

def delet_dup_s1(s1):
    """"""
    temp=''
    for x in s1:
        if x not in temp:
            temp = temp + x
    return temp
    
def delet_dup_s2(s2):
    """"""
    temp=''
    for x in s2:
        if x not in temp:
            temp = temp + x
    return temp

##def del_dup_s1(string1):
##    if len(string1)==0:
##        return []
##    elif len(string1)==1:
##        return string1[0]
##    else:
##        stored_value=del_dup_s1(string1[1:])
##        if stored_value[0] == string1[0]:
##            return stored_value
##        else:
##            return string1[0]+stored_value

def helper_func(s1,s2):
    if s1 not in s2:
        return s2
    elif s1 == s2[0]:
        return s2[1:]
    else:
        stored_value=helper_func(s1, s2[1:])
        return s2[0]+stored_value
        
#3
def jscore(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    else:
        stored_value=jscore(s1[1:],helper_func(s1[0],s2))
        if s1[0]in s2:
            return stored_value+1
        else:
            return stored_value


    
    


