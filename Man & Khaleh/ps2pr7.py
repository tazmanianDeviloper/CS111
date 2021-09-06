# 
# ps2pr7.py - Problem Set 2, Problem 7
#
# Fun with recursion, part II
#

# Problem 7-1:
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','N','O','P','R','S','T','U','V','W','X','Y','Z']

def letter_score(letter):  
    """the input is checked against the conditions and a value is returned acoordingly """
    if len(letter)==0:
        return 0
    else:
        if letter[0] in['a','e','i','l','n','o','r','s','t','u']:
            return 1
        elif letter[0] in['d', 'g']:
            return 2
        elif letter[0] in['b', 'c', 'm', 'p']:
            return 3
        elif letter[0] in['f', 'h','v','w','y']:
            return 4
        elif letter[0] in['k']:
            return 5
        elif letter[0] in['j','x']:
            return 8
        elif letter[0] in['q','z']:
            return 10
        else:
            return 0

# Problem 7-2:
def scrabble_score(word):
    """using reqursion word is reduced to 1 letter,
then that letter is passed to letter_score() as input.
Its value is concatinated to the rest in each call."""
    if len(word)==0:
        return 0
    else:
        rest=scrabble_score(word[1:])      
        if len(word)==1:
            return letter_score(word[0])    
        else:
            return rest+letter_score(word[0])

# Problem 7-3:
def add(vals1, vals2):
    """Both lists are reduced to 0 length before recursion.
If one list is empty or smaller than the other, the conditions
will handle it."""
    if len(vals1)==0 and len(vals2)==0:
        return []
    else:
        stored_value=add(vals1[1:], vals2[1:])
        if len(vals1)==1 and len(vals2)==1:
            return [vals1[0]+vals2[0]]
        elif len(vals1)==1 and len(vals2)==0:
            return [vals1[0]+0]
        elif len(vals1)==0 and len(vals2)==1:
            return [0+vals2[0]]
        else:
            return [vals1[0]+vals2[0]]+stored_value


# Problem 7-4:
def weave(s1, s2):
    """after the 3 possible base conditions, the recursion reduced the length
of both strings to 0, then at the first recall the first indices are concatinated
and saved in stored_value. After that the length of strings increase, but the
first indices are still concatinated and added to the stored_value"""
    if len(s1)==0 and len(s2)==0:
        return ''
    elif len(s1)>0 and len(s2)==0:
        return s1
    elif len(s1)==0 and len(s2)>0:
        return s2
    else:
        stored_value=weave(s1[1:], s2[1:])
        if len(s1)==1 and len(s2)==1:
            return s1[0]+s2[0]
        else:
            return s1[0]+s2[0]+stored_value
        






        
    
    
        

    
    

