

import unittest

from app import rm

import os


class TestRemove(unittest.TestCase):

    def test_rm_delete_file(self):

        open('somefile1.txt', 'w').close()

        rm('somefile1.txt')

        self.assertFalse(os.path.isfile('somefile1.txt'))


if __name__ == '__main__':
    unittest.main()









