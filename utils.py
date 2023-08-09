# A function that will time how long a function takes to run.
# This function can be used when testing functions and programs to help shave time off and make the programs run faster.

from timeit import default_timer as timer


def timefunc(func):
    def inner(*args, **kwargs):
        start = timer()
        results = func(*args, **kwargs)
        end = timer()
        message = '{} took {} seconds'.format(func.__name__, end - start)
        print(message)
        return results
    return inner
