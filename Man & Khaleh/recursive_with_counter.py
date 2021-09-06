def num_in_list(lst,rep):
    if len(lst)==0:
        return -1
    else:
        stored_value=num_in_list(lst[1:],rep)
        if lst[0]==rep:
            if stored_value==-1:
                return 1
            else:
                return stored_value+1
        else:
            return stored_value
