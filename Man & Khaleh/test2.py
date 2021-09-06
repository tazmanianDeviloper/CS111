def del_last_occu(lst,num):
    if len(lst)==0:
        return lst
    else:
        stored_value=del_last_occu(lst[:-1],num)
        if lst[-1]==num:
            return lst
        else:
            return lst+lst[-1]
            
