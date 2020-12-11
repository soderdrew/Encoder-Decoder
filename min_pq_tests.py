import unittest
from min_pq import *


class MyTestCase(unittest.TestCase):
    def test_pq(self):
        pq = MinPQ([3, 10, 231, 5])
        self.assertEqual(pq.is_empty(), False)
        self.assertEqual(pq.size(), 4)
        self.assertEqual(pq.capacity, 4)
        self.assertEqual(pq.min(), 3)
        self.assertEqual(pq.del_min(), 3)
        self.assertEqual(pq.del_min(), 5)
        self.assertEqual(pq.del_min(), 10)
        self.assertEqual(pq.del_min(), 231)
        self.assertRaises(IndexError, pq.min)
        self.assertRaises(IndexError, pq.del_min)
        self.assertEqual(pq.is_empty(), True)
        self.assertEqual(pq.num_items, 0)

    def test_pq2(self):
        pq = MinPQ()
        pq2 = MinPQ()
        self.assertEqual(pq2 == pq, True)
        pq.insert(0)
        pq.insert(0)
        pq.insert(1)
        self.assertEqual(pq.min(), 0)
        self.assertEqual(pq.del_min(), 0)
        self.assertEqual(pq.del_min(), 0)
        self.assertEqual(pq.del_min(), 1)


if __name__ == '__main__':
    unittest.main()
