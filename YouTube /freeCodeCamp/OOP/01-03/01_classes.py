"""
Assert statements check if there's a match between code and your expectations
1. Validates the arguments that we receive
2. Catch up the bugs asap before we go forward

Instance attributes are normal attributes.
Class attributes are common for every item.
"""
import csv


class Item:

    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name=str, price=float, quantity=int):
        print(f"An instance named {name} is created.")

        # Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def all_attributes(self):
        return self.name, self.price, self.quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # overwrite an attribute
        # self.price = int(self.price * Item.pay_rate)  # no matter what - the discount is from the class level
        self.price = int(self.price * self.pay_rate)    # pay_rate from instance level. nothing? then class level

    # what if we don't have any instances to call this method from?
    # use a class method!
    # 1. Instead of the "self" argument, use "cls"
    # 2. We need to use the @classmethod decorator

    @classmethod
    def instantiate_from_csv(cls):

        with open("items.csv", "r") as f:  # change the directory
            reader = csv.DictReader(f)  # we become a list of dictionaries
            items = list(reader)
            print(items)

            for item in items:
                # print(item)
                # print(item.get('name'))
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    # static method - no "self", we never send the object
    # something that is not unique for an instance
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item(\"{self.name}\", {self.price}, {self.quantity})"



Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(43.2))

"""
Before CSV:

item1 = Item("Phone", 15100, 4)
item2 = Item("MacBook", 45000, 1)
print(item1.all_attributes())
print(item1.calculate_total_price())

print(Item.pay_rate)  # print a Class attribute
print(item1.pay_rate)

print(Item.__dict__)  # all Class level attributes
print(item1.__dict__)  # all instance level attributes

print(f"{item1.price} before discount")
item1.apply_discount()
print(f"{item1.price} after discount")
item2.pay_rate = 0.95  # override the value

print(f"{item2.price} before discount")
item2.apply_discount()
print(f"{item2.price} after discount")


item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)  # 5 objects -> def __repr__ -> 5 readable objects

for i in Item.all:
    print(i.name)
"""

