def del_first_occur(string, char):
    a=len(string)
    if a==0:
        return string
    if string[0]==char:
        return string[1:]
    else:
        stored_value=del_first_occur(string[1:],char)
        if string[0]==char:
            return stored_value
        else:
            return string[0]+stored_value
