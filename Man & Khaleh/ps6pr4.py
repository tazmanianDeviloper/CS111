# ps6pr4.py (Problem Set 6, Problem 4)        
#
# Problem 4: Choosing the correct type of loop
#

#1
def log(b, n):
    """If n is bigger than its base then the division
can continue until the result is 0, but if n is smaller
than its base then we would have to check to see if it isn't
1"""
    result=0
    if n<b and n!=1:
        print('dividing',n,'by',b,'gives',n//b)
        return result+1
    else:
        while n//b!=0:
            print('dividing',n,'by',b,'gives',n//b)
            n=n//b
            result+=1
        return result

#2
def add_powers(m, n):
    """3 new variables are initialized because in each itteration
those values are changed. Power is increased by 1 until it reaches
the max value of range(m). result is printed after each itteration
and add_result is the cumilative value of all results added """
    powers=0
    result=0
    add_result=0
    for i in range(m):
        result=n**powers
        print(n,'**',powers,'=', result)
        powers+=1
        add_result+=result
    return add_result

#3
def square_evens(values):
    """For some reason Python does not recognize the type of instant value
which is an int, so when the instant value is even, we would have to assign it
to another variable to raise it. """
    r=0
    for i in range(len(values)):
        deivision_remainder=values[i]%2
        if deivision_remainder==0:
            r=values[i]
            values[i]=r**2
            
        else:
            values[i]=values[i]
            

        

                
        
    
    
        
    
        
        
    
