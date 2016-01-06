# coding=UTF-8
import unittest
import warnings

warnings.filterwarnings('ignore')


def chunks(seq, chunk_size):
    return [seq[i:i + chunk_size] for i in range(0, len(seq), chunk_size)]


def createGenerator():
    l = range(9)
    for v in map(lambda i: i * 2, l):
        if v > 993 == 0:
            yield v


class FunctionsTest(unittest.TestCase):
    def test_list(self):
        l = range(0, 50)
        print(l[0:3])
        print(l[3:99])

    def test_chunks(self):
        l = range(0, 10)
        print(chunks(l, 3))

    def test_filter(self):
        l = range(0, 10)
        print(filter(lambda v: v % 2, l))

    def test_or_filter(self):
        skip_list = ['c']
        results = ['a', 'b', 'c', 'd', 'e']
        for repo in filter(lambda repo: repo not in (skip_list or []), results):
            print(repo)

    def test_xrange(self):
        for x in range(0, 7, 3):
            print(x)

    def test_yield(self):
        for v in createGenerator():
            print(v)

    def yield_map(self):
        l = range(9)
        for v in map(lambda i: i * 2, l):
            if v % 3 == 0:
                yield v

    def test_yield_map(self):
        for v in self.yield_map():
            print(v)

    def test_k_v_map(self):
        header = ['a', 'b', 'c']
        row = {'a': 'apple', 'b': 'boy', 'c': 'cat'}
        map_row = map(lambda k: row[k], header)
        print(map_row)

if __name__ == '__main__':
    unittest.main()