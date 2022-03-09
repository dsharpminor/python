from Chef import Chef
class ChineseChef(Chef): #inside of the ChineseChef we write that we inherit from Chef

     # can do everything that a normal chef can do

    def make_fried_rice(self):
        print("The  chef makes fried rice")
        # print("Test")

    def make_special_dish(self):  #override
        print("The chef makes a special chinese dish")