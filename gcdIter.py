def gcdIter(a, b):
    bigger = min(a, b)
    while bigger >= 1:
        if a % bigger == 0 and b % bigger == 0:
            return bigger
            break
        else:
            bigger -= 1
                
            
            