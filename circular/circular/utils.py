'''This module implements utilities for Weekly circular application'''
def make_list(db_object, numberc):
    '''used to make a list of numberc cul for element in the list'''
    db_return = []
    counter = db_object.count()
    rem = counter % numberc
    i = 0
    while i < counter:
        if i < counter-rem:
            db_return.append(db_object[i:i+3])
            i = i + 3
        else:
            db_return.append(db_object[i:i+rem])
            i = i + rem
    return db_return
