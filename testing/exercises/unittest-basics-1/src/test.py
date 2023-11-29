from text import to_upper, to_word_list_isupper
import unittest


class TestText(unittest.TestCase):

    # Task 1
    def test_to_upper_returns_upper(self):

        self.assertEqual(to_upper("abcdef"), "ABCDEF", 'The strings do not match.')

    # Task 2
    def test_to_word_list_isupper_returns_true(self):

        self.assertTrue(to_word_list_isupper(['I', 'LOVE', 'YOU']), 'The function did not return true.')

    # Task 3
    def test_to_word_list_isupper_returns_flase(self):

        self.assertFalse(to_word_list_isupper(['i', 'LOVE', 'YOU']), 'The function did not return false.')

    # Task 4

    def test_to_upper_raises_error(self):

        # self.assertRaises(TypeError, to_upper, 4532)

        with self.assertRaises(TypeError):

            to_upper(4532)
            to_upper('453fhkf4545')
            # to_upper('Downtown')

    # Task 5

    def test_to_word_list_isupper_raises_error(self):

        # self.assertRaises(TypeError, to_word_list_isupper, 'Hometown')

        with self.assertRaises(TypeError):

            to_word_list_isupper('Hometown')
            to_word_list_isupper(2023)
            to_word_list_isupper(['Gametown', True])


if __name__ == '__main__':
    unittest.main()