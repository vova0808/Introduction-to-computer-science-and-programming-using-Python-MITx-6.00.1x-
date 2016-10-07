def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    lower = 0
    upper = len(aStr) - 1
    middle = (lower + upper) / 2 
    aList = list(aStr)
    target = aList[middle]
    if target == char:
        return True
    else:
        while len(aList) > 1:
            if target > char:
                upper = middle
                aList = aList[lower:upper]
                isIn(char, aList)
            elif target > char:
                lower = middle
                aList = aList[lower:upper]
                isIn(char, aList)
    return False                       
    
           
    
                            
                
            
            