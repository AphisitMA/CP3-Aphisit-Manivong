class Customer:
    Name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added product ot ", self.Name, self.lastName,"'s cart")

customer1 = Customer()
customer1.Name = "Aphisit"
customer1.lastName = "M"
customer1.addCart()

customer2 = Customer()
customer2.Name = "Kridsana"
customer2.lastName = "K"
customer2.addCart()

customer3 = Customer()
customer3.Name = "Tirapat"
customer3.lastName = "W"
customer3.addCart()