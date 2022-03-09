class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0  # a state

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This was executed {self.num_calls} times.")
        return self.func(*args, **kwargs)


"""
Class decorators are typically used when we need
to maintain and update a state.
"""

# keep track of how many times we've executed this function
@CountCalls
def say_hi():
    print("Hi")


say_hi()
say_hi()
say_hi()
"""
This was executed 1 times.
Hi
This was executed 2 times.
Hi
This was executed 3 times.
Hi
"""