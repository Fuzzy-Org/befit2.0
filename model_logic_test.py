import unittest
import numpy as np

from utils import get_fuzzy_index


class TestModelLogic(unittest.TestCase):
    def test_underweight(self):
        _, word, _, _, _ = get_fuzzy_index("Чоловіча", 80, 190, 60, "cog")
        self.assertEqual(word, "Underweight")

    def test_normal(self):
        _, word, _, _, _ = get_fuzzy_index("Жіноча", 30, 170, 70, "cog")
        self.assertEqual(word, "Normal")

    def test_overweight(self):
        _, word, _, _, _ = get_fuzzy_index("Жіноча", 30, 170, 80, "cog")
        self.assertEqual(word, "Overweight")

    def test_obese(self):
        _, word, _, _, _ = get_fuzzy_index("Жіноча", 20, 165, 110, "cog")
        self.assertEqual(word, "Obese")


if __name__ == "__main__":
    unittest.main()
