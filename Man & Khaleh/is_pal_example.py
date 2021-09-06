# is_pal function

def is_pal(s):
    '''returns True if s is a palindrome, False otherwise'''
    print('is_pal(',s,')')
    
    # base case: s is 0 or 1 character long -> return True
    if len(s) <= 1:
        print('len(s) <= 1, returning True')
        return True

    # base case: outer characters don't match: -> return False
    elif s[0] != s[-1]:
       print('s[0] != s[-1], returning False')
       return False

    # recursive case: check in "inner" string (slice off outer characters)
    else:
        is_pal_rest = is_pal(s[1:-1])
        print('is_pal_rest (',s,') returned',is_pal_rest)
        return is_pal_rest

# test cases:
##print('is_pal("") returned', is_pal(""))
##print('is_pal("a") returned', is_pal("a"))
##print('is_pal("ab") returned', is_pal("ab"))
##print('is_pal("abba") returned', is_pal("abba"))
##print('is_pal("amanaplanacanalpanama") returned', is_pal("amanaplanacanalpanama"))
print('is_pal("amanaplanacanapanama") returned', is_pal("amanapanacanalpanama"))
#

##    anna
##    civic
##    kayak
##    level
##    madam
##    mom
##    noon
##    racecar
##    radar
##    redder
##    refer
##    repaper
##    rotator
##    rotor
##    sagas
##    solos
##    stats
##    tenet
##    wow
##
##palindrome
##a word, phrase, or sequence that reads the same backward as forward
##
