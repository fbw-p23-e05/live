################################
# Do not modify this file
################################
import unittest
from warehouse import Warehouse


class TestWarehouseSingleton(unittest.TestCase):
    def setUp(self):
        self.w1 = Warehouse()
        self.w2 = Warehouse()

    def test_unique_object(self):
        self.assertTrue(self.w1 is self.w2, "The warehouse class is not a singleton")


if __name__ == '__main__':
    unittest.main()
