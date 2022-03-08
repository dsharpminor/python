from item import Item


class Phone(Item):  # inherit from Item
    # now writing the following is fine:
    # phone1 = Phone("Samsung Galaxy S10", 5000, 7)

    def __init__(self, name: str, price: float, quantity: 0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )
        print(f"(Phone instance named {name})")
        # Call to super function to have acces to all attributes / methods

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

