import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "верно")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "ошибка")


if __name__ == "__main__":
    unittest.main()