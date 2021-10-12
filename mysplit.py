def mysplit(strng):
    mylist=[]
    word=''
    
    for ch in strng:
        if ch==' ' and word:
            mylist.append(word)        
            word=''
        elif ch==' ' and word=='':
                    
            word=''
        else:
            word=word+ch
   
    if word:
            mylist.append(word) 
      
    print(mylist)

mysplit("To be or not to be, that is the question")
mysplit("To be or not to be,that is the question")
mysplit("   ")
mysplit(" abc ")
mysplit("")
