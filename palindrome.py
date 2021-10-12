def palin():
    test=input("enter the string:")
    test=test.upper()
    string=test.replace(' ','')
    print(string)
    total=int((len(string))/2)
    i=0
    while string[i]==string[len(string)-1-i]:
           i=i+1
           if i==total:
               print("its a pallindrome")
               break
    if string[i]!=string[len(string)-1-i]:
                       print("its not a palindrome")
                        
               
palin()     
        
        
