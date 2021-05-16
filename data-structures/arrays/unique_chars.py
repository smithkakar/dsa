#!/usr/local/bin/env python3
'''
Problem:
Given a string, determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and
should return True. The string 'aabcde' contains duplicate characters
and should return false.
'''

from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


def unq_chars1(s):
    return len(set(s)) == len(s)


def unq_chars2(s):
    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True


t = TestUnique()
t.test(unq_chars1)
t.test(unq_chars2)
