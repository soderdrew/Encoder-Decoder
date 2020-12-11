"""This is Project 3 where we implement Huffman Coding
with Min Heap
Course: CPE 202
Quarter: Spring 2020
Author: Drew Soderquist"""

from huffman import HuffmanNode
from min_pq import MinPQ
from huffman_bit_writer import HuffmanBitWriter
from huffman_bit_reader import HuffmanBitReader


def cnt_freq(filename):
    """opens a file an counts the frequency of chars in the file
    Args:
        filename(str): name of the input file
    Returns:
        list: 256 item list with counts of occurrences
    """
    counts = [0] * 256
    fp_file = open(filename, "r")
    lines = fp_file.readlines()
    for i in lines:
        for j in i:  # count every letter in the line
            counts[ord(j)] += 1  # counts[ord(j)] + 1
    counts[0] = 1
    fp_file.close()
    return counts


def create_huff_tree(list_of_freqs):
    """builds a huffman tree
    Args:
        list_of_freqs(list): list of frequencies from cnt_freq
    Returns:
        HuffmanNode: root node of the huffman tree
    """
    min_huff = MinPQ()  # min pq of huffman nodes
    # for i in range(len(list_of_freqs)):  # method 2: insert all huffman nodes
    for i, item in enumerate(list_of_freqs):
        if list_of_freqs[i] != 0:
            min_huff.insert(HuffmanNode(list_of_freqs[i], chr(i)))
    while min_huff.num_items != 1:  # until a root node
        low = min_huff.del_min()  # HuffmanNode
        low_2 = min_huff.del_min()  # HuffmanNode
        if ord(low.char) < ord(low_2.char):
            char = low.char
        else:
            char = low_2.char
        new_huff = HuffmanNode(low.freq + low_2.freq, char, low, low_2)
        min_huff.insert(new_huff)
    return min_huff.del_min()  # pop out root node


def create_code(root_node):
    """converts a Huffman Tree into a list of Huffman codes
    Args:
        root_node(HuffmanNode): a Huffman Tree
    Returns:
        list: 256 strings of Huffman code
    """
    huff_list = [""] * 256
    code = ""
    return create_code_helper(root_node, code, huff_list)


def create_code_helper(root_node, code, huff_list):
    """helper function for create_code
    Args:
        root_node(HuffmanNode): a Huffman Tree
        code(str): string of 0's and 1's, the Huffman code
        huff_list(list): list of Huffman codes
    Returns:
        list: 256 strings of Huffman codes
    """
    if root_node is None:  # base case, if tree is None
        return huff_list
    if root_node.left is None and root_node.right is None:  # leaf node, no children
        huff_list[ord(root_node.char)] = code  # inserts char's code
    create_code_helper(root_node.left, code + "0", huff_list)
    create_code_helper(root_node.right, code + "1", huff_list)
    return huff_list


def huffman_encode(in_file, out_file):
    """reads input, writes header and huffman code to an output file
    Args:
        in_file(file): input text file
        out_file(file): output text file
    Returns:
        N/A, writes to a file
    """
    all_codes = ""
    list_of_freqs = cnt_freq(in_file)
    header = create_header(list_of_freqs)
    tree = create_huff_tree(list_of_freqs)
    codes = create_code(tree)
    try:
        fp_read = open(in_file, "r")  # add this as a try / except
        lines = fp_read.readlines()
        for i in lines:
            for j in i:
                all_codes = all_codes + str(codes[ord(j)])
        compress_name = out_file[:len(out_file) - 4:] + "_compressed.txt"
        fp_write = open(out_file, "w", newline='')
        header += "\n"
        write_all = header + all_codes
        fp_write.write(write_all)
        fp_write.close()
        compress_file = HuffmanBitWriter(compress_name)
        compress_file.write_str(header)
        compress_file.write_code(all_codes)
        compress_file.write_code(codes[0])
        compress_file.close()
        fp_read.close()
    except FileNotFoundError:
        raise FileNotFoundError


def create_header(list_of_freqs):
    """returns header of ascii values and their frequencies
    Args:
        list_of_freqs(list): list of freqs from cnt_freq
    Returns:
        str: ascii values and their freqs
    """
    header = ""
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            header = header + str(i) + " " + str(list_of_freqs[i]) + " "
    return header


def huffman_decode(encoded_file, decode_file):
    """reads a compressed, encoded file and writes to a decode file
    Args:
        encoded_file(file): compressed file that we must decode
        decode_file(file): file that will be written to with the decoded information
    Returns:
        N/A, writes to a file
    """
    try:
        e_head = HuffmanBitReader(encoded_file)
        encode = open(encoded_file, "r")
        encode.close()
        header = e_head.read_str()
        freq_list = parse_header(header)
        tree = create_huff_tree(freq_list)
        new_tree = tree
        letters = ""
        count = 0
        for i in freq_list:
            if i != 0:
                count += int(i)
        while count > 1:
            bit = e_head.read_bit()
            if bit is True:
                new_tree = new_tree.right
            else:  # if bit is False:
                new_tree = new_tree.left
            if new_tree.left is None and new_tree.right is None:
                letters += str(new_tree.char)
                count -= 1
                new_tree = tree
        text = open(decode_file, "w", newline='')
        text.write(letters)
        text.close()
        e_head.close()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_header(header_string):
    """takes a string of a compressed encoded header and returns the original list of frequencies
    Args:
        header_string(str): compressed header string from the encoded file
    Returns:
        list: 256 strings of frequencies of characters
    """
    header_string = str(header_string)
    header_string = header_string.replace("b'", "")
    header = header_string.split()
    header_nums = []
    for j in range(len(header) - 1):
        header_nums.append(int(header[j]))
    header = header_nums
    freq_list = [0] * 256
    for i, item in enumerate(header):
        if i % 2 == 0:  # if a char
            freq_list[item] = header[i + 1]  # update at freq its # of occurance
    freq_list[0] = 1
    return freq_list
