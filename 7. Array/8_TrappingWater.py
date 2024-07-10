import time
from abc import ABC, abstractmethod
from typing import List
from utils import measure_time, get_algorithms
import random

class TrappingWater(ABC):
    @abstractmethod
    def algorithm(self, nums: List[int]) -> int:
        pass
    
# 1. Two Pointer 방법 - O(n)
class TwoPointer(TrappingWater):
    def algorithm(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        # 두 포인터가 만나기 전까지 반복
        while left < right:
            # 왼쪽 포인터, 오른쪽 포인터의 최대 갱신
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            # 오른쪽 포인터가 우위
            if left_max <= right_max:
                # 왼쪽 포인터에서 최대 높이와 현재 높이의 차이를 물의 부피로 추가 
                volume += left_max - height[left]
                # 오른쪽으로 한 칸 이동
                left += 1
            
            # 왼쪽 포인터가 우위 -> 오른쪽 포인터 갱신
            else:
                # 오른쪽 포인터에서 최대 높이와 현재 높이의 차이를 물 부피로 추가
                volume += right_max - height[right]
                # 왼쪽으로 한 칸 이동
                right -= 1
        return volume
    
# 2. Stack 방법 - O(n)
class Stack(TrappingWater):
    def algorithm(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            # 변곡점을 만날 때까지 반복 : 현재 높이 > 가장 최근의 높이
            while stack and height[i] > height[stack[-1]]:
                
                top = stack.pop()
                
                if not len(stack):
                    break
                
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
                
            stack.append(i)
        return volume

def run_tests():
    # 다양한 크기의 입력 데이터를 생성합니다.
    input_sizes = [1000, 3000, 10000]

    # 알고리즘 인스턴스 생성
    algorithms = get_algorithms(TrappingWater)

    for size in input_sizes:
        height = [random.randint(0, 10) for _ in range(size)]

        print(f"Input size: {size}")

        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm.algorithm, height)

            # 결과 검증
            result = algorithm.algorithm(height)

            print(f"  {name} time: {time_taken:.8f} seconds, result : {result}")

run_tests()