"""
Allow you to allocate and release resources precisely when you want to.
Context managers = with statements.

Open/close files, database connections, locks, etc.
"""

with open('notes.txt', 'w') as file:
    file.write("Hey!")  # "with" also closes the file


"""
# Literally the same:

file = open('notes.txt', 'w')
try:
    file.write("Hey!")
finally:
    file.close()
"""

"""
Lock:

from threading import Lock
lock = Lock()

lock.acquire()
# ...
lock.release()

with lock:
    #...
"""