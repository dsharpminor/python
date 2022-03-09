"""
1. How to share data between threads? A global variable
2. How to share data between processes?
Processes don't live in the same memory space.
-> they need special shared memory objects: Value and Array

queue.get() returns and removes the first element

3. A process pool object is used to manage multiple processes.
   It controls a pool of worker processes to which chops can be submitted.
   It can manage the available processes for you and for example
   split data into smaller chunks that can be then processed in
   parallel by different processes.
"""
import time
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
from multiprocessing import Pool
import time


def cube(number):
    return number * number * number


if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()
    # map, apply, join, close
    result = pool.map(cube, numbers)
    # creates as many processes as you have cores on your mac
    # splits into equal size chunks
    # submits this to this function

    # if you simply want to have one function executed by a pool,
    # pool.apply(cube, numbers[0])
    pool.close()
    pool.join()
    print(result)





#Queue
"""
def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)



if __name__ == "__main__":

    numbers = range(1,6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
"""

## Value, Array:
"""

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:  # lock as context manager
                # number.value += 1
                numbers[i] += 1


if __name__ == "__main__":
    lock = Lock()
    shared_number = Value("i", 0)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print("Number at beginning is", shared_number.value)
    print("Array at beginning is", shared_array[:])

    # p1 = Process(target=add_100, args=(shared_number, lock))
    # p2 = Process(target=add_100, args=(shared_number, lock))

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Number at the end is", shared_number.value)
"""
