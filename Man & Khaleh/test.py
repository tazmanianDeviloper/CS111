def double(s):
    """conditions are set to handle each case. In case of s being
of length 1 the base condition has been initialized. more than 1 in lenghth
will be recursed and concatinated to the base condition"""
    if len(s)==0:
        return ''
    else:
        rest=double(s[1:])
        if len(s)==1:
            return s[0]+s[0]
        else:
            return (s[0]+s[0])+rest
