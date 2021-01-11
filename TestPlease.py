import unittest
from main import Triangle


class TestTriangleItems(unittest.TestCase):
    def setUp(self):
        self.triangles = Triangle(3,4,5)

    def test_count_P(self):
        self.assertEqual(self.triangles.count_P(3, 4, 5), 12)

    def test_count_s(self):
        self.assertEqual(self.triangles.count_S(3, 4, 5), 6)

    def test_comming_out(self):
        self.assertEqual(self.triangles.comming_out(3, 4, 5), "Прямоугольный")

    def test_comming_out2(self):
        self.assertEqual(self.triangles.comming_out(3, 3, 4), "Равнобедренный")

    def test_comming_out3(self):
        self.assertEqual(self.triangles.comming_out(3, 3, 3), "Равносторонний")


if __name__ == '__test__':
    unittest.main()
