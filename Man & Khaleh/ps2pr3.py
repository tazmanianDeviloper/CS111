# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# More practice writing non-recursive functions
#

# even ex:'homework'
# odd ex: 'carpets'

def flipside(s):
    """The function returns both odd and even inputs,
using slicing and concatination"""
    if len(s)//2==0:
        even_mid_ind=len(s)//2
        even_flipped=s[even_mid_ind:]+s[0:even_mid_ind]
        return even_flipped
    else:
        odd_mid_ind=len(s)//2
        odd_flipped=s[odd_mid_ind:]+s[0:odd_mid_ind]
        return odd_flipped

# padded ex: ('alien', 6)
# sliced ex: ('alien', 3)

def adjust(s, length):
    """The length of s is deducted from length to determine wether
s is longer or the length. Conditions have been set to add
spaces if it is shorter or to slice it, in case it was longer"""
    if len(s)<=length:
        len_dif=length-len(s)
        padded_s=(len_dif*' ')+s
        return padded_s
    else:
        sliced_s=s[0:length]
        return sliced_s

    
        
    
