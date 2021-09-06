# ps6pr3.py (Problem Set 6, Problem 3)        
#
# Problem 3: Processing sequences with loops
#

#1
def double(s):
    """first I initialized an empty variable then I created a loop.
based on input each char of the string passes through the loop
multiplies by 2 and is added to result and finally printed."""
    result=''
    for c in s:
        result=result+c*2
    return result

#2
def weave(s1, s2):
    """After introducing the new variables, conditions are set to
account for every posibility. the difference of the bigger string
subtracted from the smaller string is saved and concatinated to the
output"""
    s_small=''
    s_big=''
    s_result=''
    s_diff=''
    if len(s1)<len(s2):
        s_small=s1
        s_big=s2
    else:
        s_small=s2
        s_big=s1
    s_diff=s_big[len(s_small):]
    for i in range(len(s_small)):
        s_result=s_result+(s_big[i]+s_small[i])
    return s_result+s_diff

#3
def index(elem, seq):
    """For every index in range of the sequence, if the sequance's instant
variable is equal to the element the loop returns the index, else the loop
will increment the index. If non of the conditions in loop are met, then loop
finishes without a retun value, which means the function will return -1"""
    for i in range(len(seq)) :
        if seq[i] == elem:
            return i
        else:
            i=+1
    return -1
        
    
        
        
        
        
    
