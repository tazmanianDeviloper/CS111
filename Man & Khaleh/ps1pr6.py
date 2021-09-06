# 
# ps1pr6.py - Problem Set 1, Problem 6
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
def mirror(s):
    """Using skip slicing, the reversed list is concatinated to the original"""
    a=s[::-1]
    return s+a

def is_mirror(s):
    """Using skip slicing, the reversed list is concatinated to the original in one order, then
in the opposite order, while both orders are simultinously compared to one-another using boolian equal function"""
    a=s[::-1]
    return a+s==s+a

def replace_end(values, new_end_vals):
    """Both sets are compared and their difference is stored in a new variable.
The second set is concatinated to the first from its first indext to the indext that coresponds to
the difference value of the comparison"""
    a=values
    b=new_end_vals
    c=len(a)-len(b)
    a[c:]=b[0:]
    return a

def repeat_elem(values, index, num_times):
    """The substring of values at its index is multiplied by num_times and saved in a new var.
the items stored in the set before the index is saved in another var, and the items after index is saved in a different var.
all three vars are concatinated in order, and saved and returned in a final var"""
    values_ind_mult=[values[index]]*num_times
    values_start=values[0:index]
    values_end=values[index+1:]
    new_values=values_start+values_ind_mult+values_end
    return new_values
    
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))
    

# optional but encouraged: add test calls for your functions below
    print ('reversed input added to the original', mirror("taymaz"))
    print ('reversed input is mirrored', is_mirror("taymaz"))
    print ('data set [1, 2, 3, 4, 5, 6, 7] is given as the first argument and [10, 11, 12] as the second: ', replace_end([1, 2, 3, 4, 5, 6, 7], [10, 11, 12]))
    print ('data set [1,2,3,4,5] is given as the first argument, 2 as second, and 4 as third: ', repeat_elem([1,2,3,4,5], 2, 4))

    
