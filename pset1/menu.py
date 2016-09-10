def item_order(order):    
    i=0
    p=''
    water=0
    hamburger=0
    salad=0
    s=order
    while s!='':
        i=s.find(' ')    
        if i==-1:
            i=len(s)
            p=s[0:]
        else :   
            p=s[0:i]
        if p=='water':
            water+=1
        elif p=='hamburger':
            hamburger+=1
        elif p=='salad' :
            salad+=1   
        s=s[i+1:len(s)] 
        
        
    s='salad:'+str(salad)+' hamburger:'+str(hamburger)+' water:'+str(water) 
    return s         