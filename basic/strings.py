# coding=UTF-8
import unittest
import os


class StringTest(unittest.TestCase):
    def test_unicode(self):
        print('Vero Personal Insurance Proposal ƒ.pdf')

    def substr_between(self, s, before, after):
        if s:
            before_index = s.find(before) + len(before)
            after_index = s.find(after, before_index)
            if len(before) < before_index < after_index:
                return s[before_index:after_index]
        return s

    def test_substr_between(self):
        file_absolute_name = os.path.realpath(__file__)
        assert "strings" == self.substr_between(str(file_absolute_name), "basic{}".format(os.path.sep), ".py")

    def test_str_rfind(self):
        file_absolute_name = os.path.realpath(__file__)
        file_name = file_absolute_name[file_absolute_name.rfind('/') + 1:]
        file_no_extension = 'host'
        print(file_absolute_name)
        print(file_name)
        extension = '' if file_no_extension.rfind('.') == -1 else file_no_extension[file_no_extension.rfind('.') + 1:]
        print('extension = %s' % extension)


if __name__ == '__main__':
    unittest.main()
