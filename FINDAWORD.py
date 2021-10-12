def faw():
    word1=input("enter a word:")
    word2=input("enter the string of letters:")
    pos=0
    for char in word1:
        if char in word2:
            pos=word2.find(char,pos)
            word1=word1.replace(char,'',1)
            if not word1:
                print("yes")
        elif char not in word2:
            print("NO")
            break

faw()        
