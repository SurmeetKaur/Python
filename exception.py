ef read_int(min, max):
        val=int(input("enter the value between -10 and 10:"))
        if val<=max and val>=min:
                return val
        else:
                raise AssertionError
            
while True:            
        try:
            y=read_int(-10,10)
            print("the number is:",y)
        except ValueError:
            print("Wrong input")
            pass
        except AssertionError:
            print("Error: the value is not within permitted range (min..max)")
            pass
        else:
            break
