
def flatten(aList):
    """
    aList : a list.
    Returns a copy of aList, which is a flattened version of aList
    """
    result = []
    for i in aList:
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result        


    
