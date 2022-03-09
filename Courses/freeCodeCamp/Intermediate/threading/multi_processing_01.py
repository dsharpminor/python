"""
Thread vs process

Running one Python interpreter - one process.
A thread - an entity within a process, also known as a light-weight process.

Processes have a separate memory space.
With multiprocessing you can process the data on different CPUs.
Only one GIL (Global Interpreter Lock) per process. Processes are easy to kill/interrupt.

Disadvantages of processes:
- a process is heavy-weight (takes more memory than starting a thread)
- since processes have a separate memory space, memory sharing isn't easy
  and inter-process communication is more complicated.

All threads in a process share the same memory, and they are light-weight.
They are great for I/O bound tasks (input/output) tasks
Threads are not interruptable and not killable -> careful with memory leaks.

Careful with race conditions! They occur when 2 or more threads want to
modify the same variable at the same time -> can easily cause bugs or crashes.
"""

from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(101):
        i = i
        time.sleep(0.1)


processes = []
num_processes = os.cpu_count()  # the number of CPUs in the system, typically 4
print(num_processes)

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers())
    processes.append(p)

# start processes
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print("end main")


