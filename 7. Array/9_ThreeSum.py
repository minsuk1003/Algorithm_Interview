import time
from abc import ABC, abstractmethod
from typing import List
from utils import measure_time, get_algorithms
import random

'''
9. 세 수의 합 : 3개의 원소의 합으로 0을 만들 수 있는 원소 찾기
'''

# 추상 클래스 정의
class ThreeSum(ABC):
    # 추상 메서드 정의
    @abstractmethod
    # 리스트와 타깃을 입력, 리스트 출력
    def algorithm(self, nums: List[int]) -> List[List[int]]:
        pass
    
class TwoPointer(ThreeSum):
    def algorithm(self, nums: List[int]) -> List[List[int]]:
        results = []
        # 정렬
        nums.sort()
        
        for i in range(len(nums)-2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 포인터 초기화
            left, right = i + 1, len(nums) - 1
            # 두 포인터가 만나기 전까지 반복
            while left < right:
                # 세 수의 합 계산 - 현재 포인터, 왼쪽 포인터, 오른쪽 포인터
                sum = nums[i] + nums[left] + nums[right]
                # 합이 음수라면, 왼쪽 포인터를 우측 이동해 합을 증가시킴
                if sum < 0:
                    left += 1
                # 합이 양수라면, 오른쪽 포인터를 좌측 이동해 합을 감소시킴
                elif sum > 0:
                    right -= 1
                # 합이 0이면, 결과에 추가
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # 왼쪽 포인터와 왼쪽 + 1 포인터가 같은 값을 가질 때까지 반복
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 오른쪽 포인터와 오른쪽 -1 포인터가 같은 값을 가질 때까지 반복
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # ??
                    left += 1
                    right -= 1
                    
        return results
                    

        
def run_tests():
    # 다양한 크기의 입력 데이터를 생성합니다.
    input_sizes = [1000, 3000, 10000]

    # 알고리즘 인스턴스 생성
    algorithms = get_algorithms(ThreeSum)

    for size in input_sizes:
        nums = [random.randint(-1, 20) for _ in range(size)]
        
        print(f"Input size: {size}")

        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm.algorithm, nums)

            # 결과 검증
            result = algorithm.algorithm(nums)

            print(f"  {name} time: {time_taken:.8f} seconds, result : {result}")

run_tests()