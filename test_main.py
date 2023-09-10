# test_main.py
import time
import unittest
from main import add

class TestMain(unittest.TestCase):

    def test_add(self):
        time.sleep(10)
        self.assertEqual(add(3, 4), 7)

if __name__ == "__main__":
    unittest.main()

