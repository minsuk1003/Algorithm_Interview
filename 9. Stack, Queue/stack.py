class Solution:
    # 20. 유효한 괄호
    # pair 딕셔너리 구성 후 스택 활용
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for p in s:
            if p in pair.values():
                stack.append(p)
            if p in pair.keys():
                if stack and stack[-1] == pair[p]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
    
    # 통과, 시간 하위권, 메모리 상위권
    
    # 21. 중복 문자 제거
    # 문제 이해 불가
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)-1, -1, -1):
            if s[i] in stack:
                pass
            else:
                stack.append(s[i])
        print(stack) # ['c', 'b', 'a']
        result = ""
        for i in range(len(stack)-1, -1, -1):
            result += stack[i]
        
        return result
    
    # 결과 : 50% 테스트 케이스 통과
    
    