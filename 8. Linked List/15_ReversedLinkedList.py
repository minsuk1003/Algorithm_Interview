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
class ReverseList(ABC):
    # Abstract method definition
    @abstractmethod
    def algorithm(self, head: ListNode) -> bool:
        pass

class Recursive(ReverseList):
    def algorithm(self, head: ListNode) -> bool:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

# Use deque for faster pop from both ends
class Repeat(ReverseList):
    def algorithm(self, head: ListNode) -> bool:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

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
    input_sizes = [5, 100]

    # Algorithm instances creation
    algorithms = get_algorithms(ReverseList)

    for size in input_sizes:
        nums = [random.randint(0, 10) for _ in range(size)]
        head = create_linked_list(nums)
        
        print(f"Input size: {size}")

        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm.algorithm, head)

            # Validate results
            result = algorithm.algorithm(head)
            
            if size == 5:
                print(f"  {name} time: {time_taken:.6f} seconds, nums: {nums}")
            else:
                print(f"  {name} time: {time_taken:.6f} seconds")

run_tests()
