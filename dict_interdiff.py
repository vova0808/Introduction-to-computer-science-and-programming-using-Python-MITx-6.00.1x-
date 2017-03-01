a = {1:30, 2:20, 3:30}
b = {1:40, 2:50, 3:60}

def f(a, b):
    return a > b



def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above. 
    """

    def intersect(d1, d2):
        result = {}
        for key in d1.keys():
            if key in d2.keys():
                result[key] = f(d1[key], d2[key])
        return result

    def difference(d1, d2):
        result = {}
        for key, value in d1.items():
            if not key in d2.keys():
                result[key] = value
        for key, value in d2.items():
            if not key in d1.keys():
                result[key] = value
        return result        
        

    result_a = intersect(d1, d2)
    result_b = difference(d1, d2)
    return (result_a, result_b)

print(dict_interdiff(a, b))
                

    
    
