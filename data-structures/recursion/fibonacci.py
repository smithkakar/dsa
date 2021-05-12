from nose.tools import assert_equal

class TestFib(object):
    
    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(1), 1)
        assert_equal(solution(23), 28657)
        print('Passed all tests.')

# Complexity is exponential O(2^n)
def fib_recursive(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Recursion
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dynamic(n, cache=None):
    if cache is None:
        cache = [None] * (n+1)

    if n == 0 or n == 1:
        return n
    if cache[n] != None:
        return cache[n]
    cache[n] = fib_dynamic(n-1) + fib_dynamic(n-2)

    return cache[n]

def fib_iterative(n):
    
    a = 0
    b = 1
    
    for i in range(n):
        a, b = b, a + b
        
    return a

t = TestFib()
t.test(fib_recursive)
t.test(fib_dynamic)
t.test(fib_iterative)