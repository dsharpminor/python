import functools


def start_end_decorator_01(func):  # decorator function
    def wrapper(*args, **kwargs):  # wrapper function (inside of decorator)
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


# !r is not really needed in an f-String,
# but it is basically repr()
# and repr() returns a printable representation of the given object

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug                    # executed first
@start_end_decorator_01   # executed inside of @debug
def say_hello(name):      # executed inside of @start_end_decorator_01
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello("Anastasia")

"""
Calling wrapper('Anastasia')
start
Hello Anastasia
end
'wrapper' returned 'Hello Anastasia'
"""