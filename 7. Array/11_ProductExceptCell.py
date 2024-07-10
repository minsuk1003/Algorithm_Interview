import time
from abc import ABC, abstractmethod
from typing import List
from utils import measure_time, get_algorithms
import random

'''
11. 자신을 제외한 배열 곱
'''

# 추상 클래스 정의
class ProductExceptCell(ABC):
    # 추상 메서드 정의
    @abstractmethod
    # 리스트와 타깃을 입력, 리스트 출력
    def algorithm(self, nums: List[int]) -> List[int]:
        pass
    
class TwoPointer(ProductExceptCell):
    def algorithm(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)- 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
        
def run_tests():
    # 다양한 크기의 입력 데이터를 생성합니다.
    input_sizes = [5, 1000, 3000, 10000]

    # 알고리즘 인스턴스 생성
    algorithms = get_algorithms(ProductExceptCell)

    for size in input_sizes:
        nums = [random.randint(-10, 10) for _ in range(size)]
        
        print(f"Input size: {size}")

        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm.algorithm, nums)

            # 결과 검증
            result = algorithm.algorithm(nums)
            
            if size == 5:
                print(f"  {name} time: {time_taken:.8f} seconds, nums:{nums}, result: {result}")
            else:
                print(f"  {name} time: {time_taken:.8f} seconds")

run_tests()