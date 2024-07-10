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
class Merge(ABC):
    # Abstract method definition
    @abstractmethod
    def algorithm(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

# 1. 재귀 구조로 연결
class Recursive(Merge):
    def algorithm(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.algorithm(l1.next, l2)
        return l1

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
    algorithms = get_algorithms(Merge)

    for size in input_sizes:
        l1 = [random.randint(0, 10) for _ in range(size)]
        l1 = create_linked_list(l1)
        l2 = [random.randint(0, 10) for _ in range(size)]
        l2 = create_linked_list(l2)
        print(f"Input size: {size}")

        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm.algorithm, l1, l2)

            # Validate results
            result = algorithm.algorithm(l1, l2)
            
            if size == 5:
                print(f"  {name} time: {time_taken:.8f} seconds")
            else:
                print(f"  {name} time: {time_taken:.8f} seconds")

run_tests()
