
pin=input("Please enter the Pin to ENTER: ")

while pin == "7580":
    option=input("""Would you like to ADD or FETCH?
                    ADD = 1 
                    FETCH = 2
                    quit=Q: """)
    if option == '1':
        nickname=input("Enter a nickname for this save: ")
        email=input("Enter your email: ")
        pwd=input("Enter your password: ")
    elif option=='2':
        nick=input("Enter the nickname: ")
    elif option=="Q" or "q":
        break
    else: 
        print("You have selected wrong option!")
        

