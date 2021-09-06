#
# ps2pr6.py - Problem Set 2, Problem 6
#
# list comprehensions
#

# Problem 6-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [x+x for x in range(5)]

# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [w[1:2] for w in words]

# part c
lc3 = [word[::-1]+word[::-1] for word in ['hello', 'bye', 'no']]

# part d
lc4 = [x*x for x in range(1, 10) if (x**2)%4==0]

# part e
lc5 = [c == 'b' or c=='u' for c in 'bu be you']


# Problem 6-2: Put your definition of the function below.
def powers_of(base, count):
    """base has been raised to every x in the range of count"""
    lc6=[base**x for x in range(count)]
    return lc6

# Problem 6-3: Put your definition of the function below.
def shorter_than(n, wordlist):
    """Exvery x that has a lenght that is less than 4 is printed"""
    lc7=[x for x in wordlist if len(x)<n]
    return lc7
       
# The code below prints the values of your expressions
# from 6-1. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(1, 6):
        lc_var = 'lc' + str(n)
        if lc_var in dir():
            print(lc_var, '=', eval(lc_var))
