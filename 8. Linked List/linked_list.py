from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 13. 팰린드롬 연결 리스트
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        while True:            
            array.append(head.val)
            if head.next != None:
                head = head.next
            else:
                break
        
        left, right = 0, len(array) - 1

        while left < right:
            if array[left] != array[right]:
                return False
            left += 1
            right -= 1
        return True
    
    # 결과 : 통과, 시간 복잡도 : O(N), 실행 시간 : 287ms, 상위 30%
    
    # 14. 두 정렬 리스트 병합
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result

        while list1 and list2:
            if list1.val >= list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
    
        return result.next
    
    # 결과 : 통과, 시간 복잡도 : O(N), 실행 시간 : 37ms, 상위 35%
    
    # 15. 역순 연결 리스트
    # 리스트를 pop하고 이를 연결 리스트에 하나씩 추가하는 방식으로 구현
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # 스택에 노드 값 저장
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        # 스택에서 값을 꺼내며 새로운 역순 연결 리스트 생성
        new_head = ListNode(stack.pop())  # 첫 노드 생성
        curr = new_head
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        
        return new_head
    
    # 결과 : 통과, 실행 시간에서는 상위 20% 기록했지만, 메모리는 매우 비효율적
    
    # 16. 두 수의 덧셈
    # 연결 리스트를 차례대로 덧셈한 뒤에 string 타입으로 변환해 하나씩 거꾸로 삽입
    def addTwonumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum, l2_sum = 0, 0
        i, j = 0, 0
        while l1 and l2:
            l1_sum += (l1.val * 10 ** i)
            l2_sum += (l2.val * 10 ** j)
            l1 = l1.next
            l2 = l2.next
            i += 1
            j += 1
        while l1:
            l1_sum += (l1.val * 10 ** i)
            l1 = l1.next
            i += 1
        while l2:
            l2_sum += (l2.val * 10 ** j)
            l2 = l2.next
            j += 1

        sum = l1_sum + l2_sum
        sum_str = str(sum)
        
        result = ListNode(sum_str[len(sum_str)-1])
        curr = result
        for i in range(len(sum_str)-2, -1, -1):
            curr.next = ListNode(sum_str[i])
            curr = curr.next
        
        return result
    
    # 결과 : 통과, 실행 시간에서는 약간 손해, 메모리는 상위 10% 이내
    
    
    # 17. 페어의 노드 스왑
    # node를 두 개씩 이동시키며, 값 교환
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            if node.next is None:
                return head
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        
        return head 
    
    # 결과 : 통과, 실행 시간, 메모리 모두 평균
    
    # 18. 홀짝 연결 리스트
    # 실패
    
    # 19. 역순 연결 리스트 2
    # left, right 사이가 아닌 원소는 연결 리스트에 저장
    # left, right 사이의 원소는 스택에 저장, 마지막에 pop하면서 연결 리스트에 저장
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        result = head
        curr = result
        stack = []
        sequence = 1
        while node:
            # reverse node : push stack
            if (sequence >= left and sequence <= right):
                stack.append(node.val)
                node = node.next
                # end of reverse node : pop stack and insert into linked list
                if sequence == right:
                    while stack:
                        curr.val = stack.pop()
                        curr = curr.next
                sequence += 1
                continue
            # not reverse node : insert into linked list
            curr.val = node.val
            curr = curr.next
            node = node.next
            sequence += 1

        return result
    
    # 결과 : 통과, 실행 시간 보통, 메모리 손해
