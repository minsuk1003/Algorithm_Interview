import time
from abc import ABC, abstractmethod
from typing import List, Deque
from utils import measure_time, get_algorithms
import random
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Abstract class definition
class Palindrome(ABC):
    # Abstract method definition
    @abstractmethod
    def algorithm(self, head: ListNode) -> bool:
        pass

class ListConvert(Palindrome):
    def algorithm(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # Convert to list
        while node is not None:
            q.append(node.val)
            node = node.next

        # Check if it is a palindrome
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

# Use deque for faster pop from both ends
class DequeConvert(Palindrome):
    def algorithm(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def run_tests():
    # Various sizes of input data
    input_sizes = [5, 1000, 3000, 10000]

    # Algorithm instances creation
    algorithms = get_algorithms(Palindrome)

    for size in input_sizes:
        nums = [random.randint(0, 10) for _ in range(size)]
        head = create_linked_list(nums)
        
        print(f"Input size: {size}")

        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm.algorithm, head)

            # Validate results
            result = algorithm.algorithm(head)
            
            if size == 5:
                print(f"  {name} time: {time_taken:.8f} seconds, nums: {nums}, result: {result}")
            else:
                print(f"  {name} time: {time_taken:.8f} seconds")

run_tests()
