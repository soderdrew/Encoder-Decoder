"""HuffmanNode
CPE202
Author:
    Drew Soderquist
"""


class HuffmanNode:
    """A HuffmanNode is one of None or HuffmanNode
    Attributes:
        freq(int): frequency of character in a file
        char(str): a character
        left(HuffmanNode): left subtree of a HuffmanTree
        right(HuffmanNode): right subtree of a HuffmanTree
    """
    def __init__(self, frequency, char=None, left=None, right=None):
        self.freq = frequency
        self.char = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        """checks if two HuffmanNodes are equivalent"""
        return (self.freq == other.freq and self.char == other.char
                and self.left == other.left and self.right == other.right)

    def __repr__(self):
        """String representation of a HuffmanNode"""
        return f"HuffmanNode(char: {self.char}, freq: {self.freq}, " \
               f"left: {self.left}, right: {self.right})"

    def __lt__(self, other):
        """Implementing this function let you compare two HuffmanNode objects
         with < in your program
        Args:
            other (HuffmanNode): other HuffmanNode object to be compared with self
        Returns:
            bool: True if self <= other, else return False
        """
        if self.freq < other.freq:
            return True
        if self.freq == other.freq:
            if ord(self.char) < ord(other.char):  # what if char's are the same?
                return True
        return False
