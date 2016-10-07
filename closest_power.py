def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 1
    exponentials = [1] #list for exponential numbers, starting point - 1 
    numbers = [base] #list for numbers equals base ** exponent, starting point - base
    num = int(num)
    flag = False
    if num == 1:
        return 0
    elif base * 2 > num:
        return 0    
    
            
    while not flag:
        exponent += 1
        numbers.append(base ** exponent)
        exponentials.append(exponent)
        
        if base ** exponent > num:
            flag = True
    

    numbers.append(num)
    
    numbers.sort()
    
    
    index = numbers.index(num)
    if index == 0:
        closest_number = numbers[1]
    else:
        previous_number = numbers[index-1]
        next_number = numbers[index+1]
        diff1 = num - previous_number
        diff2 = next_number - num
        if diff1 == diff2:
            closest_number = previous_number
        elif diff2 < diff1:
            closest_number = next_number
        else:
            closest_number = previous_number
    numbers.remove(num)
    
    target = numbers.index(closest_number)
    return exponentials[target]                        

    
    
            
        
        
    
        
    

    

    
    
    

        
        
        
        
    
    
