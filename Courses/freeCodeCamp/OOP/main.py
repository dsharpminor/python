from item import Item
from phone import Phone


item1 = Phone("MyItem", 5000, 7)
# getters, setters, encapsulation

item1.send_email()

print(item1.price)
# item1.read_only_name = "other"  # AttributeError: can't set attribute
# _name = protected, can be seen in autocomplete options when typing
# __name = private, cannot be seen in autocomplete options when typing

# item1.name after creating a setter works

print(Item.all)
print(Phone.all)

"""
1. Encapsulation
        Restricting direct access to some of our attributes in a program
        Getters        @property
        Setters        @x.setter
 
       @property
       def name(self):
           print("Getter is working")
           return self.__name
   
       @name.setter
       def name(self, value):
           print("Setter is working")  
           self.__name = value  
            
2. Abstraction
        Show necessary attributes, hide the unnecessary ones
        Some utility __methods are called from a different method
        Hide utility methods, don't hide the methods that are meant to be used by programmer
  
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
   
3. Inheritance
        Allows to reuse code across classes
        
        main.py
        from item import Item
        from phone import Phone
        
        item.py      
        class Item:  
        
        phone.py
        from item import Item
        class Phone(Item):  # inherit from Item              
        
4. Polymorphism
        Polymorphism is Many forms
        Example: len() can accept arguments of different types
                 and returns the object accordingly
                 
        name = "Anastasia"
        my_list = ["one", "two", "three]
        print(len(name))      # String
        print(len(my_list))   # List
        
        
        override = change value
        overload = use different types

"""


"""                                                                                                                                                  
phone1 = Item("Samsung Galaxy S10", 5000, 7)                                                                                                         
phone1.broken_phones = 1                                                                                                                             
phone2 = Item("Samsung Galaxy S20", 5000, 7)                                                                                                         
phone2.broken_phones = 0                                                                                                                             

print(phone1.calculate_total_price())                                                                                                                
phone3 = Phone("Samsung Galaxy S20", 5000, 7, 1)                                                                                                     
"""

"""                                                                                                                                                  
CSV                                                                                                                                                  

Item.instantiate_from_csv()                                                                                                                          
print(Item.all)                                                                                                                                      
print(Item.is_integer(43.2))                                                                                                                         

"""

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
