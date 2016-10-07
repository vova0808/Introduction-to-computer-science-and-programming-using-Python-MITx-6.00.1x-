def dotProduct(listA, listB):

    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''

    
    result = 0
    index = 0
    while index <= len(listA) - 1:
        result += listA[index] * listB[index]
        index += 1
    return result    
