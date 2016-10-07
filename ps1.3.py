s = 'mfvqhano'
index = 0
current = s[index]
lst = []
result = None
for letter in s[1:]:
    if letter >= current[-1]:
        current += letter
        index += 1
    else:
        lst.append(current)
        index += 1
        current = s[index]
lst.append(current)
result = lst[0]
for i in lst:
    if len(i) > len(result):
        result = i
print(result)        

  
                     
            

   
        
    
       
       
    
        

        
            
    
        
        
