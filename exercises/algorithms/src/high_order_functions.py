# check it out here: https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence


def rec_fib(n):
    """inefficient recursive function as defined, returns Fibonacci number"""
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n


def mem_fib(n, _cache={}):
    """efficiently memoized recursive function, returns a Fibonacci number"""
    '''
    this example takes advantage of the fact that a default keyword argument is the same object every time the 
    function is called, but normally you wouldn't use a mutable default argument for exactly this reason
    '''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n


if __name__ == '__main__':
    print(dir(2))
