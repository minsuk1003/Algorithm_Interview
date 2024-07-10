import time
from abc import ABC, abstractmethod
from typing import List
from utils import measure_time, get_algorithms

'''
7. 두 수의 합 : 리스트에서 원소 간의 덧셈이 타깃인 원소 찾기
'''

# 추상 클래스 정의
class TwoSum(ABC):
    # 추상 메서드 정의
    @abstractmethod
    # 리스트와 타깃을 입력, 리스트 출력
    def algorithm(self, nums: List[int], target: int) -> List[int]:
        pass
    
# 1. Brute Force 방법 : 모든 조합 검사 - O(n^2)
class BruteForce(TwoSum):
    def algorithm(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 2. IN을 사용한 방법 - O(n)
class UseIn(TwoSum):
    def algorithm(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
        return []

# 3. 딕셔너리를 사용한 방법 - O(1) ~ O(n)
class KeyValue(TwoSum):
    def algorithm(self, nums: List[int], target: int) -> List[int]:
        # 딕셔너리에 저장하므로 더 빠른 조회가 가능
        nums_map = {}
        
        # 딕셔너리에 값과 인덱스 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
 
# 4. 조회 구조 개선 - O(1) ~ O(n)
class KeyValueImprove(TwoSum):
    def algorithm(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        # 하나의 for문으로 합쳐 저장하면서 조회함
        for i, num in enumerate(nums):
            # 찾으면 바로 빠져나옴
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i   
            
# 5. 투 포인터 이용 - O(n)
class TwoPointer(TwoSum):
    def algorithm(self, nums: List[int], target: int) -> List[int]:
        # 초기 포인터를 양 끝에 위치
        left, right = 0, len(nums) - 1
        # 같을 때까지 반복
        while not left == right:
            # 합이 타깃보다 작으면 왼쪽 포인터를 오른쪽으로 이동 : 합을 더 크게
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타깃보다 크면 오른쪽 포인터를 왼쪽으로 이동 : 합을 더 작게
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
        
def run_tests():
    # 다양한 크기의 입력 데이터를 생성합니다.
    input_sizes = [1000, 3000, 10000]

    # 알고리즘 인스턴스 생성
    algorithms = get_algorithms(TwoSum)

    for size in input_sizes:
        nums = list(range(size))
        target = nums[-1] + nums[-2]  # 리스트의 마지막 두 요소의 합을 target으로 설정

        print(f"Input size: {size}")

        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm.algorithm, nums, target)

            # 결과 검증
            result = algorithm.algorithm(nums, target)
            assert result == [size - 2, size - 1], f"Failed for {name} with size {size}"

            print(f"  {name} time: {time_taken:.8f} seconds")

run_tests()