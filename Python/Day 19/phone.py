from item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, damaged):
        super().__init__(name, price, quantity)
        self.damaged = damaged

item1 = Item("Computer", 1200, 2)
item2 = Phone("Phone", 300, 20, 3)

print(f"{item2.name} price is {item2.price}")
print(f"{item2.name} total price is", item2.calculate_total_price())
item2.apply_discount()
print(f"{item2.name} price after discount is {item2.price}")

print(f"\n\n{item2.damaged} is the number of damaged {item2.name}")

#we can use the bellow for loop to print all the names of the items in our class
#for instances in Item.all:
#    print(instances.name)
