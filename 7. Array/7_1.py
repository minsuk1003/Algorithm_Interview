import time
from typing import List
from utils import measure_time

class twoSumSolution:
    # 1. Brute Force 방법 : 모든 조합 검사
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    # 2. in을 활용한 방법            
    def use_in(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]
        return []

def run_tests():
    # 다양한 크기의 입력 데이터를 생성합니다.
    input_sizes = [100, 500, 1000, 2000, 5000]

    # 두 알고리즘의 실행 시간을 저장할 리스트
    brute_force_times = []
    use_in_times = []

    two_sum = twoSumSolution()

    for size in input_sizes:
        nums = list(range(size))
        target = nums[-1] + nums[-2]  # 리스트의 마지막 두 요소의 합을 target으로 설정

        # Brute Force 방법 실행 시간 측정 및 결과 검증
        bf_time = measure_time(two_sum.brute_force, nums, target)
        bf_result = two_sum.brute_force(nums, target)
        brute_force_times.append(bf_time)

        # in을 활용한 방법 실행 시간 측정 및 결과 검증
        ui_time = measure_time(two_sum.use_in, nums, target)
        ui_result = two_sum.use_in(nums, target)
        use_in_times.append(ui_time)

        # 결과 검증
        assert bf_result == ui_result == [size - 2, size - 1], f"Failed for size {size}"

    # 결과를 출력
    for size, bf_time, ui_time in zip(input_sizes, brute_force_times, use_in_times):
        print(f"Input size: {size} - Brute Force: {bf_time:.6f} seconds, Use in: {ui_time:.6f} seconds")

run_tests()