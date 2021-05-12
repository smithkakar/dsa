from nose.tools import assert_equal

class TestPerm(object):
    
    def test(self, solution):
        
        assert_equal(sorted(solution('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        print('All test cases passed.')

def permute(s):
    output = []
    if len(s) == 1:
        output = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                output += [letter + perm]

    return output

t = TestPerm()
t.test(permute)
