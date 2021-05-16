#!/usr/local/bin/env python3
from nose.tools import assert_equal

'''
An anagram is when the two strings can be written using the
exact same letters (so you can just rearrange the letters to get a different
phrase or word).
'''


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


def anagram1(s1, s2):

    # remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


def anagram2(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # edge case
    if len(s1) != len(s2):
        return False

    count = {}

    # add counts
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # subtract counts
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # count will be 0 for each character if two strings are anagrams
    for k in count:
        if count[k] != 0:
            return False

    return True


t = AnagramTest()
t.test(anagram1)
t.test(anagram2)
