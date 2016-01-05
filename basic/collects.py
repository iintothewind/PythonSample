# coding=UTF-8
import unittest
from collections import defaultdict
from collections import namedtuple


class CollectionsTest(unittest.TestCase):
    def test_defaultdict(self):
        md = defaultdict(set)
        md[1].add('a')
        md[1].add('b')
        md[1].add('a')
        md[2].add('c')
        md[2].add('c')
        md[2].add('d')
        md[3].add('f')
        for k, v in {k: v for k, v in md.items() if len(v) > 1}.items():
            print("%s = %s" % (k, v))

    def test_namedtuple(self):
        colored_point = {}
        point = namedtuple('Point', ['x', 'y'])
        colored_point[point(x=0, y=0)] = '00'
        colored_point[point(x=0, y=1)] = '01'
        colored_point[point(x=1, y=0)] = '10'
        colored_point[point(x=1, y=1)] = '10'
        for k, v in colored_point.items():
            print('type(k) == {}, k.x == {}, k.y == {}, v == {}'.format(type(k), k.x, k.y, v))
