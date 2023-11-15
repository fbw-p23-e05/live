################################
# Do not modify this file
################################
import unittest
from factory_class import WorkerFactory
from worker import Packager, DeliveryMan


class TestWarehouseSingleton(unittest.TestCase):
    def test_create_object_Packager(self):
        try:
            p = WorkerFactory.create_object("packager")
            self.assertIsInstance(p, Packager, "The method create_object doesn't create a Packager object")
        except Exception as e:
            self.assertTrue(False, str(e) + "\ncreate_object method not implemented correctly")

    def test_create_object_DeliveryMan(self):
        try:
            d = WorkerFactory.create_object("delivery")
            self.assertIsInstance(d, DeliveryMan, "The method create_object doesn't create a DeliveryMan object")
        except Exception as e:
            self.assertTrue(False, str(e) + "\ncreate_object method not implemented correctly")


if __name__ == '__main__':
    unittest.main()
