from typing import List

class MySolution:
    # 7. 두 수의 합 : 리트코드 1번
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # 결과 : 통과, 시간 복잡도 : O(N^2), 실행 시간 : 1681ms
    
    # 8. 빗물 트래핑 : 리트코드 42번
    def trap(self, height: List[int]) -> int:
        result = 0
        local_max_list = []
        # local maximum 인덱스 찾기
        for i in range(len(height)-2):
            if (i == 0) and (height[i] > height[i+1]):
                local_max_list.append(i)
            if (height[i] <= height[i+1]) and (height[i+1] > height[i+2]):
                local_max_list.append(i+1)
        
        if height[len(height)-2] < height[len(height)-1]:
            local_max_list.append(len(height)-1)

        # 비교해서 최종 local maximum 인덱스 찾기
        for i in range(len(local_max_list)-1):
            if height[local_max_list[i]] >= height[local_max_list[i+1]]:
                for j in range(1, (local_max_list[i+1] - local_max_list[i])):
                    if height[local_max_list[i+1]] - height[local_max_list[i+1]-j] > 0:
                        result += (height[local_max_list[i+1]] - height[local_max_list[i+1]-j])
            else:
                for j in range(1, (local_max_list[i+1] - local_max_list[i])):
                    if height[local_max_list[i+1]] - height[local_max_list[i+1]-j] > 0:
                        result += (height[local_max_list[i+1]] - height[local_max_list[i+1]-j])

        return result
    
    # 결과 : 86/322 통과
    
    # 9. 세 수의 합 : 리트코드 15번
    # 시간 내 풀이 실패
    
    # 10. 배열 파티션 1 : 리트코드 561번
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
    
    # 결과 : 통과, 실행 시간 : 203ms, 상위 2% 
        
    # 11. 자신을 제외한 배열의 곱 : 리트코드 238번
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for index in range(len(nums)):
            for i in range(1, len(nums)):
                result[index] *= nums[(i+index) % len(nums)]
            
        return result
    
    # 결과 : 18/24 통과, 6/24 시간 초과
    
    
