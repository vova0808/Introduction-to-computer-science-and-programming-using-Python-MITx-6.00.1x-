def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is flattened version of aList
    '''
    result = []
    if len(aList) == 0:
        return aList
    else:
        for item in aList:
            if type(item) == list:
                result.extend(flatten(item))
            else:
                result.append(item)
    return result                    
        
        
        