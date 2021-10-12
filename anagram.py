def ana():
    word1=input("enter the first word:")
    word2=input("enter the second word:")

    for char in word2:
        if char in word1:
            
            word1=word1.replace(char,'',1)
            print(word1)
            if not word1:
                print("anagram")
            
        elif char not in word1:
            print("not anagram")
            break
       
ana()    
