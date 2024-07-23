from typing import List
import collections

class Solution:
    # 29. 보석과 돌
    # 보석을 리스트로 변환하여 in으로 찾는 방법
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in range(len(stones)):
            if stones[i] in list(jewels):
                count += 1
        return count
    
    # 통과, 시간 복잡도 : O(N * M)

    # 30. 중복 문자 없는 가장 긴 부분 문자열
    # 중복 문자가 들어왔을 때, 해당 문자 이전까지 모두 삭제하는 방법
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        stack = []
        for i in range(len(s)):
            if s[i] in stack:
                stack = stack[stack.index(s[i])+1:]
            stack.append(s[i])
            if len(stack) >= max_count:
                max_count = len(stack)
        return max_count
    
    # 통과
    
    # 31. 상위 k 빈도 요소
    # collections 모듈의 Counter 클래스를 활용하는 방법
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [i[0] for i in counter.most_common(k)]
    
    # 통과

    
