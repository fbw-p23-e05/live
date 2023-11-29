



import unittest
import app
from app import rm

from unittest import mock



class TestRemove(unittest.TestCase):

    # Task 2

    @mock.patch('app.os.path') # 2nd
    @mock.patch('app.os') # 1st
    def test_rm_delete_file(self, mock_os, mock_path):

        mock_path.isfile.return_value = True
        # mock_path.isfile.return_value = None

        rm('somefile1.txt')

        mock_os.remove.assert_called_with('somefile1.txt')

        # self.assertTrue(mock_path.isfile('somefile1other2222.txt'))

        # self.assertIsNone(mock_path.isfile('somefile1.txt'))
        
        # assert mock_path.isfile('somefile1.txt') is None


    # Task 3

    @mock.patch('app.os.path') # 2nd
    @mock.patch('app.os') # 1st
    def test_rm_delete_file_not_exist(self, mock_os, mock_path):

        mock_path.isfile.return_value = False
        # mock_os.chown.return_value = 'Michael'

        rm('anotherfile.txt')

        # mock_os.remove.assert_called_with('somefile1.txt')
        self.assertFalse(mock_os.remove.called)
        # mock_os.remove.called

    # Task 5
    @mock.patch('app.os.path') # 2nd
    @mock.patch('app.os') # 1st
    def test_rm_delete_file_not_exist(self, mock_os, mock_path):

        mock_path.isfile.return_value = False

        with self.assertRaises(FileNotFoundError):

            rm('anotherfile.txt')


if __name__ == '__main__':
    unittest.main()









