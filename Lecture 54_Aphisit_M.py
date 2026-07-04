def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        print("Invalid Username or Password")
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        totalPrice = int(input("Total Price : "))
        print("Price including Vat", vatCalculate(totalPrice))
    elif userSelected == 2:
        print("Price including Vat", priceCalculat())
    else:
        print("Invalid menu selected")
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculat():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

while not login():
    pass
showMenu()
menuSelect()
