from threading import Thread
import time
def square_numbers_2():
    for i in range(101):
        i = i + 1
        time.sleep(0.1)

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create processes
    for i in range(num_threads):
        t = Thread(target=square_numbers_2())
        threads.append(t)

    # start processes
    for t in threads:
        t.start()

    # join
    for t in threads:
        t.join()  # wait and block the main thread until the thread is complete

    print("end main")