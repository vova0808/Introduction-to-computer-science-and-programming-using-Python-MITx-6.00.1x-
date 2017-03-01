def f(i):
    return i + 2

def g(i):
    return i > 5



def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    
    """
    if len(L) == 0:
        return -1
    else:
        index = len(L) - 1
        while index >= 0:
            if not g(f(L[index])):
                L.remove(L[index])
            index -= 1
        return max(L)    
