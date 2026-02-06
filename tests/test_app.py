# test_app.py

import unittest
from app import calculate

class TestApp(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(calculate(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
