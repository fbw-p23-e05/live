from django.test import TestCase


class ExampleTestClass(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print("Run once to create non-modified data to be used by all class methods."
              "Use this to create objects or data that is not to be modified by any of the test methods.")
        pass
    
    def setUp(self):
        print("Run once for every test method. Used when you want to have a"
              " clean set of data for each test method.")
        pass
    
    def tearDown(self):
        print("Run after all each test is completed to clean up any data.")
        pass
    
    def test_false_is_false(self):
        print("false is supposed to be false")
        self.assertFalse(False)
    
    def test_view_return_a_redirect(self):
        self.assertTrue(True)
        