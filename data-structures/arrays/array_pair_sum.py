#!/usr/local/bin/env python3
'''
Given an integer array, output all the unique pairs that sum up to a specific value k.
Example:
pair_sum([1,3,2,2],4)
would return 2 pairs:
(1,3)
(2,2)
'''

from nose.tools import assert_equal


class TestPair(object):

    def test(self, sol):
        assert_equal(
            sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        assert_equal(sol([1], 4), "")
        print('ALL TEST CASES PASSED')


def pair_sum(arr, k):

    if len(arr) < 2:
        return ""

    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    return len(output)
    # print('\n'.join(map(str,list(output))))


t = TestPair()
t.test(pair_sum)
