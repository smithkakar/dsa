#!/usr/local/bin/env python3
'''
Problem:
Given a string of words, reverse all the words. For example:

Example:
'This is the best'
Return:
'best the is This'

We will remove all leading and trailing whitespace. So that inputs such as:
'  space here'  and 'space here      '
both become:
'here space'

Solution:
We could take advantage of Python's abilities and solve the problem
with the use of split() and some slicing or use of reversed.
'''

from nose.tools import assert_equal


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '),
                     'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


def rev_word1(s):
    return " ".join(reversed(s.split()))


def rev_word2(s):
    return " ".join(s.split()[::-1])


def rev_word3(s):
    # Split the words manually

    words = []
    spaces = [' ']
    length = len(s)

    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])

        i += 1

    return " ".join(reversed(words))


t = ReversalTest()
t.test(rev_word1)
t.test(rev_word2)
t.test(rev_word3)
