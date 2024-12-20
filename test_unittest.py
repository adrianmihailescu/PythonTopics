import unittest

def add(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 4), 5)

if __name__ == "__main__":
    unittest.main()
