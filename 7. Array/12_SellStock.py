import time
from abc import ABC, abstractmethod
from typing import List
from utils import measure_time, get_algorithms
import random
import sys

'''
12. 한 번의 거래로 낼 수 있는 최대 이익 산출
'''

# 추상 클래스 정의
class SellStock(ABC):
    # 추상 메서드 정의
    @abstractmethod
    # 리스트와 타깃을 입력, 리스트 출력
    def algorithm(self, prices: List[int]) -> int:
        pass
    
class BruteForce(SellStock):
    def algorithm(self, prices: List[int]) -> int:
        max_price = 0
        
        # 가격 반복
        for i, price in enumerate(prices):
            # 현재 가격부터 가격 반복
            for j in range(i, len(prices)):
                # 최대 가격 계산
                max_price = max(prices[j] - price, max_price)
        
        return max_price

class MinMax(SellStock):
    def algorithm(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값, 최댓값 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit
    
def run_tests():
    # 다양한 크기의 입력 데이터를 생성합니다.
    input_sizes = [5, 1000, 3000, 10000]

    # 알고리즘 인스턴스 생성
    algorithms = get_algorithms(SellStock)

    for size in input_sizes:
        nums = [random.randint(0, 10) for _ in range(size)]
        
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