import time
from custom_palindrome import isPalindrome


def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print ('func:%r args:[%r : no_of_iteratom = %r] took: %2.4f sec' %
               (f.__name__, kw.get("msg", ""),
                kw.get("no_of_time", 1), te - ts))
        return result

    return timed


@timeit
def run_test(f, data=None, no_of_time=10, msg=None):
    data = ["madam", "maxam", "ußßu"] if data is None else data
    data = data * no_of_time
    for row in data:
        if f(str(row)):
            pass

run_test(isPalindrome, data=["ma@am", "@madam@", "1raxer1",
                             123455, "malayalam"],
         msg="with multiple combination")
run_test(isPalindrome, no_of_time=10000, msg="run for 10000")
run_test(isPalindrome, no_of_time=100000, msg="run for 100000")
run_test(isPalindrome, no_of_time=1000000, msg="run for 1000000")
run_test(isPalindrome, data=["m$ada@m" * 10000000],
         no_of_time=1, msg="test with 1-billon-characters")
run_test(isPalindrome, data=[
         "ma@am", "test", "best", "@madam@", "1raxer1", 123455, "malayalam"],
         no_of_time=10000, msg="with multiple combination run for 10000")
