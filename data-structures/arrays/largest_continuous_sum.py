'''
Problem:
Given an array of integers (positive and negative),
find the largest continuous sum.

Solution:
If the array is all positive, then the result is simply the sum of all numbers.
The negative numbers in the array will cause us to need to begin
checking sequences.

The algorithm is, we start summing up the numbers and store in a
current sum variable. After adding each element, we check whether the
current sum is larger than maximum sum encountered so far. If it is,
we update the maximum sum. As long as the current sum is positive,
we keep adding the numbers. When the current sum becomes negative,
we start with a new current sum. Because a negative current sum will only
decrease the sum of a future sequence.
Note that we don’t reset the current sum to 0 because
the array can contain all negative integers.
Then the result would be the largest negative number.
'''

from nose.tools import assert_equal

class LargestContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]), 9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]), 29)
        assert_equal(sol([-1,1]), 1)
        assert_equal(sol([-11,-2,-1,-3,-4,-10,-10,-10,-1]), -1)
        print('ALL TEST CASES PASSED')
        
def largest_cont_sum(arr):

    # edge case
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum

t = LargestContTest()
t.test(largest_cont_sum)
