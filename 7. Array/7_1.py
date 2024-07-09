from typing import List
from utils.utils import measure_time

class BruteForceSolution:
    def twoSum(self, nums, target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# test data
nums = [i for i in range(10000)]                
target = 19999

brute_force = BruteForceSolution()
brute_force_time = measure_time(brute_force.twoSum, nums, target)
print(f"{brute_force_time:.6f}")