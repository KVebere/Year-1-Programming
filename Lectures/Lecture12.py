class Shopping:
    def __init__(self):
        self.total = 0

    def spend(self, amount):
        self.total += amount
        return self.total
    
    def checkout(self):
        if self.total >= 100:
            discount = 0.25 * self.total
        elif self.total >= 50:
            discount = 0.1 * self.total
        else:
            discount = "No discount applied."
        
        newTotal = self.total - discount
        output = f"Discount Amount: {discount},\n" 
        output += f"New amount: {newTotal}"
        return output


   
def testShopping():
    shopping = Shopping()
    print(shopping.total)
    #Debug print
    print(shopping.spend(50))
    print(shopping.spend(60))
    print(shopping.checkout())

#testShopping()    
    
class Shopping2:
    def __init__(self):
        self.total = 0

    def spend(self, amount):
        self.total += amount
        return self.total
    
    def checkout(self):
        discount = 0
        if self.total >= 100:
            discount = 0.25 * self.total
        elif self.total >= 50:
            discount = 0.1 * self.total
        else:
            discount = 0
        
        newTotal = self.total - discount
        output = f"Discount Amount: {discount},\n" 
        output += f"New amount: {newTotal}"
        self.total = 0
        return output

def testShopping2():
    shopping = Shopping2()
    shopping.spend(50)
    shopping.spend(60)
    print(shopping.checkout())
    shopping.spend(20)
    print(shopping.checkout())
    shopping.spend(75)
    print(shopping.checkout())
testShopping2()