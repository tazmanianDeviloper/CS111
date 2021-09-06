def mystery(vals):
    a = vals[0]
    b = vals[1]
    c = vals[2]
    
    if a >= b:
        if b < c:
            print('round')
        else:
            print('found')
    elif b >= c:
        print('mound')
        if b < a:
            print('pound')
        elif a < c:
            print('ground')
        elif b == c:
            print('wound')
    else:
        if a == c:
            print('hound')
        print('zounds')
    print('redound')

mystery([2,8,8])



        
