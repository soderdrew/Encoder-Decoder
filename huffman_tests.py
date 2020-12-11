"""This is Project 3 where we implement Huffman Coding
with Min Heap
Course: CPE 202
Quarter: Spring 2020
Author: Drew Soderquist"""

import unittest
import filecmp
from huffman_coding import cnt_freq, create_huff_tree, create_code, huffman_encode, huffman_decode
from min_pq import MinPQ


# from huffman import HuffmanNode


class TestList(unittest.TestCase):
    def test_huffman(self):
        huff_tree1 = create_huff_tree(cnt_freq("test1.txt"))
        huff_tree2 = create_huff_tree(cnt_freq("test1.txt"))
        self.assertEqual(huff_tree1, huff_tree2)
        print(huff_tree1.left.left)
        self.assertEqual(huff_tree1.left.left.freq, 3)
        # huff_tree3 = HuffmanNode(2, "a")
        # huff_tree4 = HuffmanNode(2, "b")
        # self.assertEqual(huff_tree3.freq, 2)
        # self.assertEqual()
        # self.assertEqual(huff_tree1.left.left, "HuffmanNode(char: s, freq: 3, left: None, right: None)")

    def test_freq(self):
        freq_list = cnt_freq("test1.txt")
        anslist = [0] * 256
        anslist[100:112] = [1, 3, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
        self.assertEqual(freq_list[0], 1)
        self.assertEqual(freq_list[100:112], anslist[100:112])

    def test_create_huff_tree_1(self):
        freq_list = cnt_freq("test1.txt")
        huff_tree = create_huff_tree(freq_list)
        left = huff_tree.left
        numchars = 16
        self.assertEqual(huff_tree.freq, 17)
        self.assertEqual(left.left.char, "s")
        self.assertEqual(left.left.freq, 3)
        self.assertEqual(huff_tree.right.right.right.char, "e")

    def test_create_code_1(self):
        freq_list = cnt_freq("test1.txt")
        huff_tree = create_huff_tree(freq_list)
        code = create_code(huff_tree)
        print("d", code[ord("d")])
        print("s", code[ord("s")])
        print("l", code[ord("l")])
        self.assertEqual(code[ord('d')], '11011')
        self.assertEqual(code[ord('s')], '00')
        self.assertEqual(code[ord('l')], '1001')

    def test_encode_soln(self):
        huffman_encode("test1.txt", "encode_test1_soln.txt")
        self.assertEqual(1, 1)

    def test_encode_actual(self):
        huffman_encode("test1.txt", "encode_test_test1.txt")
        self.assertEqual(1, 1)

    def test_both_encodes(self):
        self.assertTrue(filecmp.cmp("encode_test1_soln.txt", "encode_test_test1.txt"))

    def test_decode_and_encode_1(self):
        huffman_encode("test1.txt", "encode_test1_soln.txt")
        huffman_decode("encode_test1_soln_compressed.txt", "test_decode.txt")
        self.assertTrue(filecmp.cmp("test_decode.txt", "test1.txt"))

    def test_blank_file(self):
        huffman_encode("blank.txt", "encode_blank.txt")
        huffman_decode("encode_blank_compressed.txt", "blank_decode.txt")
        self.assertTrue(filecmp.cmp("blank.txt", "blank_decode.txt"))

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
