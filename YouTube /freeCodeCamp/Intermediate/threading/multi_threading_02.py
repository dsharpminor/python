from threading import Thread, Lock
import time


"""
Use Locks to prevent Race Condition when
two threads try to modify one value
at the same time.

before: lock.acquire()
after: lock.release()

or

with lock:
"""

db_value = 0


def increase(lock):
    global db_value
    with lock:
        local_copy = db_value
        # processing
        local_copy += 1  # race condition,
        # both try to modify the value simultaneously
        time.sleep(0.1)
        db_value = local_copy

"""
    lock.acquire()
    local_copy = db_value
    # processing
    local_copy += 1  # race condition,
    # both try to modify the value simultaneously
    time.sleep(0.1)
    db_value = local_copy
    lock.release()
"""

if __name__ == "__main__":

    lock = Lock()
    print("start value", db_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value", db_value)
    print("end main")
