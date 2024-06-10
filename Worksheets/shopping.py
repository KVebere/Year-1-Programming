class Shopping:
    def __init__(self):
        self.total = 0
    
    def spend(self, amount):
        self.total += amount

    def checkout(self):
        if self.total <= 100:
            self.total = self.total * 0.75
            discount = 25
        elif self.total > 50:
           self.total = self.total * 0.9
           discount = 10
        else:
            discount = 0
        print(f"Discount: {discount}, total: {self.total}")
