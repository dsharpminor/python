from threading import Thread, Lock, currentThread
import time
from queue import Queue

"""
queue = FIFO (a line of customers)
    in a threading environment:
    # q.get
        some processing
    # q.task_done()
    
    q.join() - block the main thread and wait until all
    elements in our queue are processed
    
    
    q.get() and q.put() are thread-safe
    # q.empty()  # check if it is empty

"""


def worker(q, lock):
    while True:
        value = q.get()
        # processing
        with lock:
            print(f"in {currentThread().name} got {value}")
        q.task_done()
        # instead of daemon we could have used a condition:
        # if ...:
        #   break


if __name__ == "__main__":

    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        # a background thread that will die when the main thread dies
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    first = q.get()
    print(first)

    print('end main')
    # we have an infinite loop, but it dies here
    # because of the daemon thread
    # we could have used an event insteas


"""

Multiple statements in the same line? without a lock

in Thread-1 got 1in Thread-2 got 2
in Thread-3 got 3in Thread-5 got 4
in Thread-7 got 5
in Thread-7 got 6

in Thread-1 got 7

in Thread-3 got 8
in Thread-3 got 9
"""