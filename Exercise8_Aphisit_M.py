usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234" :
    print("Welcome to >>> Work Together Cafe")
    print("----OUR MANU----")
    print("1. Espresso 50 THB")
    print("2. Americano 70 THB")
    print("3. Latte 80 THB")
    print("4. Cappuccino 90 THB")
    print("5. Green Tea 100 THB")
    print("What do you want to drink?")
    userSelected = int(input(">>"))
    if userSelected ==1:
        price = int(input("Number of Cup: "))
        result = price*50
        print("Total is =", result,"THB")
    elif userSelected == 2:
        price = int(input("Number of Cup: "))
        result = price*70
        print("Total is =", result,"THB")
    elif userSelected == 3:
        price = int(input("Number of Cup: "))
        result = price*80
        print("Total is =", result,"THB")
    elif userSelected == 4:
        price = int(input("Number of Cup: "))
        result = price*90
        print("Total is =", result,"THB")
    elif userSelected == 5:
        price = int(input("Number of Cup: "))
        result = price*100
        print("Total is =", result,"THB")
else :
    print("Your Username or Password are wrong!!!")