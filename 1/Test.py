import unittest
from main import CustomList


class Test(unittest.TestCase):
    
    def setUp(self):
        self.a = CustomList([1, 3])
        self.b = CustomList([2, 1])

    def test_checkneq(self):
        c = CustomList([1,0,2])
        d = self.a.check_n_equalize(c)
        self.assertEqual(d, 3)
        self.assertEqual(self.a.new_lst, [1, 3, 0])
        self.assertEqual(self.a.new_other, [1, 0, 2])

    def test_checknsum(self):
        c = CustomList([1, 0, 2])
        d = self.a.check_n_sum(c)
        self.assertEqual(d, [4, 3])

    def test_add(self):
        self.assertEqual((self.a + [2, 1, 2]).lst, CustomList([3, 4, 2]).lst)
        self.assertEqual(([2, 1] + self.a).lst, CustomList([3, 4]).lst)
        self.assertEqual((self.a + self.b).lst, CustomList([3, 4]).lst)
        
    def test_sub(self):
        self.assertEqual((self.a - [2, 1, -1]).lst, CustomList([-1, 2, 1]).lst)
        self.assertEqual(([2, 1] - self.a).lst, CustomList([1, -2]).lst)
        self.assertEqual((self.a - self.b).lst, CustomList([-1, 2]).lst)

    def test_lt(self):
        self.assertEqual(self.a < [1, 1, 0], False)
        self.assertEqual([1, 0] < self.a, True)
        self.assertEqual(self.a < self.b, False)

    def test_gt(self):
        self.assertEqual(self.a > [1, 1, 0], True)
        self.assertEqual([1, 0] > self.a, False)
        self.assertEqual(self.a > self.b, True)

    def test_le(self):
        c = CustomList([4,0])
        self.assertEqual(self.a <= [1, 0, 3], True)
        self.assertEqual([1, 3] <= self.a, True)
        self.assertEqual(self.a <= c, True)
        self.assertEqual(self.a <= [1, 1], False)
        self.assertEqual([1, 0] <= self.a, True)
        self.assertEqual(self.a <= self.b, False)

    def test_ge(self):
        c = CustomList([4, 0])
        self.assertEqual(self.a >= [1, 0, 3], True)
        self.assertEqual([1, 3] >= self.a, True)
        self.assertEqual(self.a >= c, True)
        self.assertEqual(self.a >= [1, 1], True)
        self.assertEqual([1, 0] >= self.a, False)
        self.assertEqual(self.a >= self.b, True)

    def test_eq(self):
        c = CustomList([4, 0])
        self.assertEqual(self.a == [1, 0, 3], True)
        self.assertEqual([1, 3] == self.a, True)
        self.assertEqual(self.a == c, True)

    def test_ne(self):
        self.assertEqual(self.a != [1, 1, 1], True)
        self.assertEqual([1, 2] != self.a, True)
        self.assertEqual(self.b != self.a, True)

if __name__ == '__main__':
    unittest.main()