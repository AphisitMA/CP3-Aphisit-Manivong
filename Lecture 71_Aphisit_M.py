menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("---My Food---")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    print("Total Price:",totalPrice)

while True:
    menuName = input("Please enter a menu option: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please enter a price: ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()