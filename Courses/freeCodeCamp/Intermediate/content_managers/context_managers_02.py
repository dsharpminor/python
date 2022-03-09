# implement your own context manager

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("enter")
        # allocate our resource
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:  # aka if it exists
            self.file.close()
            if exc_type is not None:
                print("exception has been handled")
        # print("exc:", exc_type, exc_val)
        # exc: <class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'somemethod'
        print("exit")
        return True


with ManagedFile("notes.txt") as file:
    print("do some stuff")
    file.write("\n one more thing")
    file.somemethod()  # it doesn't exist
print("continuing")



"""
Sure, your specific decorator lets you do something just before and after a function call,
provided no exception is raised, or you explicitly handle exceptions. But you could also
use a decorator to add an attribute to the function object, or to update some kind of registry.
Or to return something entirely different and ignore the original function. Or to produce
a wrapper that manipulates the arguments passed in, or the return value of the original
function. A context manager can't do any of those things.

A context manager on the other hand lets you abstract away try: ... finally: constructs, 
in that 
no matter how the block exits, you get to execute some more code at the end of the block.

Use decorators when you require to do something to or with functions or classes when
they are defined. Use context managers when you want to clean up or take other actions
after a block ends. 
"""