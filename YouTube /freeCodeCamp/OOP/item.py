import csv


class Item:  # parent class
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        print(f"An instance named {name} is created.")

        # Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def all_attributes(self):
        return self.name, self.__price, self.__quantity

    def calculate_total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        # overwrite an attribute
        # self.price = int(self.price * Item.pay_rate)  # no matter what - the discount is from the class level
        self.__price = int(
            self.__price * self.pay_rate)  # pay_rate from instance level. nothing? then class level

    # what if we don't have any instances to call this method from?
    # use a class method!
    # 1. Instead of the "self" argument, use "cls"
    # 2. We need to use the @classmethod decorator

    @classmethod
    def instantiate_from_csv(cls):

        with open("items.csv", "r") as f:  # change the directory
            reader = csv.DictReader(
                f)  # we become a list of dictionaries
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
        return f"{self.__class__.__name__}(\"{self.name}\", {self.__price}, {self.__quantity})"  #

    @property  # getter
    def name(self):
        print("Getter is working")
        return self.__name

    @name.setter  # setter
    def name(self, value):
        if len(value) > 15:
            raise Exception("The name is too long")
        else:
            print("Setter is working")
            self.__name = value

    @property
    def price(self):
        return self.__price

    def __connect(self):
        pass

    def __prepare_body(self):
        pass

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()





"""    @property  # Property Decorator = read-only attribute
    def read_only_name(self):
        return "AAA"
"""

