# 
# ps1pr3.py - Problem Set 1, Problem 3
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
def cube(x):
    return x**3

def convert_to_inches(yard, feet):
    """Checks for Null posibilties"""
    if yard > 0 and feet > 0:
        inches=((yard*3)+feet)*12
        return inches
    elif yard <= 0:
        yard=0
        inches=((yard*3)+feet)*12
        return inches
    elif feet <= 0:
        feet=0
        inches=((yard*3)+feet)*12
        return inches   

def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """Assigns paired values from this function to the previous one"""
    height_inch=(convert_to_inches(height_yds, height_ft))  
    width_inch=(convert_to_inches(width_yds, width_ft))
    area = height_inch * width_inch
    return area

def median(a,b,c):
    """All possibilities accounted for"""
    if (a >= b >= c) or (a <= b <= c):
        median = b
    
    if (b >= a >= c) or (b <= a <= c):
        median = a
    
    if (a >= c >= b) or (b <= c <= a):
        median = c
####################################### 
    if (a >= b) and (a >= c):
            largest = a
            
    if (b >= a) and (b >= c):
            largest = b
            
    if (c >= b) and (c >= a):
            largest = c
####################################### 
    if (a <= b) and (a <= c):
            smallest = a
            
    if (b <= a) and (b <= c):
            smallest = b
            
    if (c <= b) and (c <= a):
            smallest = c
####################################### 
    if a == smallest and b  ==  largest:
        median = c
        
    if b  ==  smallest and a  ==  largest:
        median = c    
####################################### 
    if a  ==  smallest and c == largest:
        median = b
        
    if c == smallest and a == largest:
        median = b
####################################### 
    if b == smallest and c == largest:
        median = a
        
    if c == smallest and b == largest:
        median = a 
            
    return median        

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite of(-8) is: ', opposite(-8))
    print('The cube of (3) is: ', cube(3))
    print('The inch values of (-2,5) are: ', convert_to_inches(-2,5))
    print('An area with the fallowing diameters (1,2,1,2) is: ', area_sq_inches(1,2,1,2), 'inches')
    print('The median among (11,30,8) is: ' , median(11,30,8)) 

    # optional but encouraged: add test calls for your functions below
