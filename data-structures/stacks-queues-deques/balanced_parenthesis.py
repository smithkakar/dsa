#!/usr/local/bin/env python3
'''
Problem Statement
Given a string of opening and closing parentheses, check whether it’s balanced.
We have 3 types of parentheses: round brackets: (), square brackets: [],
and curly brackets: {}. Assume that the string doesn’t contain any other
character than these, no spaces words or numbers.
As a reminder, balanced parentheses require every opening parenthesis
to be closed in the reverse order opened.
For example ‘([])’ is balanced but ‘([)]’ is not.
'''

from nose.tools import assert_equal


class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')


def check_balanced_paren(s):
    # check if even number of brackets
    if len(s) % 2 != 0:
        return False

    open_parens = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # stack to track open parentheses in string
    stack = []

    for paren in s:
        if paren in open_parens:
            stack.append(paren)
        else:
            # when there is no opening paren against current closing paren
            if len(stack) == 0:
                return False

            last_open_paren = stack.pop()

            if (last_open_paren, paren) not in matches:
                return False

        # in case there were opened parens that were not closed
    return len(stack) == 0


print(check_balanced_paren('[](){([[[]]])}'))
t = TestBalanceCheck()
t.test(check_balanced_paren)
