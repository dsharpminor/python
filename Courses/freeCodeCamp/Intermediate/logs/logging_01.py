import logging

# here we can change what is being printed:

# level=logging.DEBUG - from which log we want it to be printed
# then we can add the time and the format of the error

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                                datefmt="%m/%d/%Y %H:%M:%S")

# by default our logger is the root logger, but it is better to create your own

"""
There are 5 different log levels:
- debug
- info
- warning
- error
- critical
"""
#                                           by default:
logging.debug("This is a debug message")  # doesn't print anything
logging.info("This is an info message")  # doesn't print anything
logging.warning("This is a warning message")  # WARNING:root:This is a warning message
logging.error("This is an error message")  # ERROR:root:This is an error message
logging.error("This is a critical message")  # ERROR:root:This is a critical message
