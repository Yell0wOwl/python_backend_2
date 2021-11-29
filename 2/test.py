import unittest

from main import CustomClass


class Test(unittest.TestCase):
    def setUp(self):
        self.obj = CustomClass()

    def test_attributes(self):
        self.assertFalse(hasattr(self.obj, "x"))
        self.assertTrue(hasattr(self.obj, "custom_x"))
        self.assertFalse(hasattr(self.obj, "val"))
        self.assertTrue(hasattr(self.obj, "custom_val"))
        self.assertFalse(hasattr(self.obj, "line"))
        self.assertTrue(hasattr(self.obj, "custom_line"))

if __name__ == "__main__":
    unittest.main()



