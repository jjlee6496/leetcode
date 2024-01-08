class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        # Move to the next nodes if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        
        current = current.next
    
    # Reverse the result linked list
    result = None
    while dummy.next:
        temp = dummy.next
        dummy.next = temp.next
        temp.next = result
        result = temp
    
    return result