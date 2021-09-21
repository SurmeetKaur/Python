##TIC TAC TOE

board={'1':' ','2':' ','3':' ',
     '4':' ','5':' ','6':' ',
     '7':' ','8':' ','9':' '}
 

def displayboard(board):
       print("+----+----+----+")
       print("|    |    |    |")
       print("| "+board['1']+"  | "+board['2']+"  | "+board['3']+"  |")
       print("|    |    |    |")
       print("+----+----+----+")
       print("|    |    |    |")
       print("| "+board['4']+"  | "+board['5']+"  | "+board['6']+"  |")
       print("|    |    |    |")
       print("+----+----+----+")
       print("|    |    |    |")
       print("| "+board['7']+"  | "+board['8']+"  | "+board['9']+"  |")
       print("|    |    |    |")
       print("+----+----+----+")


def play():
    count=0
    turn='X'

    
    for i in range(10):
        displayboard(board)
        print("its "+turn+" turn\n","select your move:",end="")
        move=input()
        if board[move]!=" ":
                      print("space is already filled\n")
                    
                      
        else:
                   
                   board[move]=turn
                   count+=1
                   if count>=5 and board['1']==board['2']==board['3']!=" " or board['4']==board['5']==board['6']!=" " or board['7']==board['8']==board['9']!=" " or board['1']==board['4']==board['7']!=" " or board['2']==board['5']==board['8']!=" " or board['3']==board['6']==board['9']!=" " or board['1']==board['5']==board['9']!=" " or board['3']==board['5']==board['7']!=" ":
                              displayboard(board)
                              print("Game Over")
                              print(" **** " +turn + " won ****")
                              break
                              
                   elif count==9:
                             displayboard(board)
                             print("Game Over")
                             print("its a tie")
                             break
                             
                   elif turn=='X':
                                turn='0'
                         
                   else:
                               turn='X'
                   continue
                   


play()              

        
