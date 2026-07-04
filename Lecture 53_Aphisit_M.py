def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

price = int(input("Please enter your price: "))
totalPrice = vatCalculate(price)
print(totalPrice)