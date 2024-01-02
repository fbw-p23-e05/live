import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')

    # Task 1 : This test involves randomized value. So we may not get the exact value every time we run the test.
    def test_rnd_1(self):
        self.assertIn(rnd(2, 20), range(2, 21))


    # Task 2: This test also involves randomized value. We may not be sure if the value will be out of range in other test runs.
    def test_rnd_2(self):

        result = rnd(2, 20)

        if result > 20 or result < 2:
            self.fail(f'{result} out-of-range')


if __name__ == '__main__':
    unittest.main()