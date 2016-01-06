# coding=UTF-8
import unittest
import os


class StringTest(unittest.TestCase):
    def test_unicode(self):
        print('Vero Personal Insurance Proposal ƒ.pdf')

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