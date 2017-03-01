def deep_reverse(L):
    """
    Assumes L is a list of lists whose elemenst are ints.
    Mutate L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    for l in L:
        l.reverse()
    L.reverse()

    
    
