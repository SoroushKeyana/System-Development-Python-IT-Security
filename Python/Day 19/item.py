class Item:
    #we can have an attribute here which is reachable to all instances. If there is for example an attribute in the instance then it will choose that otherwise it chooses this one.
    discount_rate = 0.8

    #the bellow list is to store all items in a list and then in the init method we can append all items
    all = []
    def __init__(self, name: str, price: float, quantitiy=0) -> None:
        #using assert to make sure the user enters positive values
        assert price >= 0, f"Price {price} should not be negative"

        self.name = name
        self.prnice = price
        self.quantitiy = quantitiy
        #bellow code is to append items to all list 
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantitiy
    
    def apply_discount(self):
        self.price = self.price * self.discount_rate