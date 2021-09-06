def del_last_occu(lst,num):
    """the input is checked in the first base then in the second base,
if conditions are not met, recursion begins. The list is sliced with each itteration,
the bases are check again and returned to be stored in the stored_value"""
    a=len(lst)
    if a==0:
        return lst
    if lst[-1]==num:
        return lst[0:-1]
    else:
        stored_value=del_last_occu(lst[:-1],num)       
        if lst[-1]==num:
            return stored_value
        else:
            return stored_value+[lst[-1]]
