#!/usr/local/bin/env python3
'''
This is a classic recursion problem: Given a target amount n and a list (array) of distinct coin values, 
what's the fewest coins needed to make the change amount.

For example:
If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
1+1+1+1+1+1+1+1+1+1
5 + 1+1+1+1+1
5+5
10

With 1 coin being the minimum amount.
Solution:
This is a classic problem to show the value of dynamic programming. 
We'll show a basic recursive example and show why it's actually not the best way to solve this problem.
'''

from nose.tools import assert_equal


class TestCoins(object):

    def check(self, solution):
        coins = [1, 5, 10, 25]
        assert_equal(solution(45, coins), 3)
        assert_equal(solution(23, coins), 5)
        assert_equal(solution(74, coins), 8)
        print('Passed all tests.')


def coin_recursion(target, coins):
    min_coins = target

    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_recursion(target-i, coins)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


'''
The problem with this approach is that it is very inefficient! 
It can take many, many recursive calls to finish this problem and 
it is also inaccurate for non standard coin values (coin values that are not 1,5,10, etc.)
'''


def coin_dynamic(target, coins, cache=None):
    if cache is None:
        cache = [0]*(target+1)
    min_coins = target

    if target in coins:
        cache[target] = 1
        return 1
    elif cache[target] > 1:
        return cache[target]
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_dynamic(target-i, coins, cache)

            if num_coins < min_coins:
                min_coins = num_coins
                # reset cache for known results
                cache[target] = min_coins

    return min_coins


test = TestCoins()
test.check(coin_dynamic)
