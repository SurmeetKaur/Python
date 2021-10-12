def dol():
    dob=input("enter the date of birth:")
    sum=0
    
    for ch in dob:
        sum=sum+int(ch)
    sum=str(sum)
    if len(sum)>1:
            
                 print(int(sum[0])+int(sum[1]))
    else:
            print(sum)
 
        

dol()    
    
