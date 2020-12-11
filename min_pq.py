"""This is Lab 7 where we cover Minimum Priority Queue ADT
with Min Heap
Course: CPE 202
Quarter: Spring 2020
Author: Drew Soderquist"""


class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity(int): the capacity of the queue
        num_items(int): the number of items in the queue
        arr(list): an array which contains the items in the queue
    """

    def __init__(self, arr=None):
        """initializes an object of MinPQ
        Args:
            arr(list): the default value is None
        """
        if arr is not None:
            self.arr = arr
            self.num_items = len(self.arr)
            self.capacity = len(self.arr)
            self.heapify()
        else:
            self.arr = [None] * 2
            self.num_items = 0
            self.capacity = 2

    def __eq__(self, other):
        """checks if two objects are equal"""
        return (self.arr == other.arr and self.capacity == other.capacity
                and self.num_items == other.num_items)

    def __repr__(self):
        """returns the string representation of the MinPQ"""
        return f"MinPQ(arr: {self.arr}, capacity: {self.capacity}," \
               f" num_items: {self.num_items})"

    def heapify(self):
        """convert the array, self.arr, into a min heap"""
        length = self.num_items
        i = self.index_parent(length - 1)
        while i >= 0:
            self.shift_down(i)
            i -= 1
        return

    def insert(self, item):
        """inserts an item into the queue
        Args:
            item(any): an item to be inserted into the queue
        """
        self.enlarge()
        # print(item)
        if self.num_items == 0:
            self.arr[0] = item
        else:
            self.arr[self.size()] = item
        self.shift_up(self.num_items)
        self.num_items += 1
        return

    def del_min(self) -> any:
        """deletes the minimum item in the queue
        Args:
            N/A
        Returns:
            int or HuffmanNode: smallest integer value in the min heap or lowest HuffmanNode
        Raises:
            IndexError: Raises IndexError when the queue is empty
        """
        if self.num_items == 0:
            raise IndexError
        # self.shrink()
        min_item = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.num_items -= 1
        self.shift_down(0)
        return min_item

    def min(self) -> any:
        """returns the minimum item in the queue without deleting the item
        Returns:
            any: the minimum item
        Raises:
            IndexError: Raises IndexError when the queue is empty
        """
        if self.num_items == 0:
            raise IndexError
        return self.arr[0]

    def is_empty(self):
        """checks if the queue is empty
        Returns:
            bool: True if empty, False otherwise
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """returns the number of items in the queue
        Returns:
            int: returns the number of items, self.num_items, in the queue
        """
        return self.num_items

    def shift_up(self, idx):
        """shift up an item in the queue using tail recursion
        Args:
            idx(int): the index of the item to be shifted up in the array
        """
        iparent = self.index_parent(idx)
        if iparent < 0 or self.arr[iparent] < self.arr[idx]:
            return
        temp = self.arr[idx]
        self.arr[idx] = self.arr[iparent]
        self.arr[iparent] = temp
        return self.shift_up(iparent)

    def shift_down(self, idx):
        """shifts down an item in the queue using tail recursion
        Args:
            idx(int): index of the item to be shifted down in the array
        """
        if self.num_items < idx:
            return
        imin = self.index_minchild(idx)
        if imin < 0 or self.arr[idx] < self.arr[imin]:
            return
        self.arr[idx], self.arr[imin] = self.arr[imin], self.arr[idx]
        return self.shift_down(imin)

    def enlarge(self):
        """enlarges the array
        """
        if self.capacity == self.num_items:
            newarr = [None] * (self.capacity * 2)
            for i in range(self.num_items):
                newarr[i] = self.arr[i]
            self.arr = newarr
            self.capacity = self.capacity * 2
        return self.arr

    def shrink(self):
        """shrinks the array
        """
        if self.capacity / self.num_items >= 4:
            newarr = [None] * (self.capacity // 2)
            for i in range(self.num_items):
                newarr[i] = self.arr[i]
            self.arr = newarr
            self.capacity = self.capacity // 2
        return self.arr

    def index_minchild(self, i):
        """compute the index of the child with the lowest value
        Args:
            i(int): index
        Returns:
            int: index of the min child
        """
        if self.num_items - 1 < index_left(i):  # no children
            return -1
        if self.num_items - 1 < index_right(i):  # one child
            return index_left(i)
        if self.arr[index_left(i)] < self.arr[index_right(i)]:  # two children
            return index_left(i)
        return index_right(i)

    def index_parent(self, i):
        """compute the index of the parent
        Args:
            i(int): index
        Returns:
            int: index of parent
        """
        idx = (i - 1) // 2
        if self.arr[idx] is None:
            return -1
        return idx


def index_left(i):
    """compute the index of the left child
    Args:
        i(int): index
    Returns:
        int: index of the left child
    """
    return 2 * i + 1


def index_right(i):
    """compute the index of the left child
    Args:
        i(int): index
    Returns:
        int: index of the left child
    """
    return 2 * i + 2
