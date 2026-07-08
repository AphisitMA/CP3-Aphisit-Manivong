menuList = []
def showBill():
    print("---My Food---")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1],"THB")

while True:
    menuName = input("Please enter a menu option: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please enter a price: ")
        menuList.append([menuName, menuPrice])
print(menuList)
showBill()