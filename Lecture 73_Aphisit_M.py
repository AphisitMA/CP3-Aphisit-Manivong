systemMenu = {"ข้าวหมกไก่": 45, "ข้าวมันไก่": 40, "ข้าวมันไก่ผสม": 50, "ข้าวมันไก่พิเศษ": 50}
menuList = []
def showBill():
    print("----My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += menuList[number][1]
        print("TotalPrice=", totalPrice)
while True:
    menuName = input("Please enter your menu option: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

print(menuList)
showBill()