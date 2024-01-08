# Linked list

유연하게 크기 변경이 가능한 자료구조. 데이터를 자유롭게 삽입 삭제가 가능하다. 집합의 단위를 List, 각 요소의 단위를 Node라고 한다.
![img1](https://lamarr.dev/images/algorithm/linkedlist01.jpg)
## vs array

array: 인덱스와 그에 대응하는 value로 이루어진 구조

데이터 엑세스 속도: array - O(1) 리스트는 최소 한번은 순회를 거쳐야 하기 때문에 O(N)

데이터 삽입/삭제: Linked list-O(1) , array - O(N)

## Single Linked List

```jsx
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### add

```python
# 연결 리스트의 노드 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 노드들을 연결
node1.next = node2
node2.next = node3

# 연결 리스트를 순회하며 값 조회
current = node1  # 연결 리스트의 시작 노드부터 시작
while current:
    print(current.val)  # 현재 노드의 값 출력
    current = current.next  # 다음 노드로 이동
```

### delete

```python
# 연결 리스트의 노드 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 노드들을 연결
node1.next = node2
node2.next = node3

# node2 삭제하기
node1.next = node3
```

### reverse

```python
# 연결 리스트의 노드 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 노드들을 연결
node1.next = node2
node2.next = node3

# 뒤집기
dummy = ListNode()
current = node1

while current:
	temp = current.next # 현재 노드의 다음 노드를 임시로 저장
	current.next = dummy.next # 현재 노드의 다음을 더미의 다음으로 연결
	dummy.next = current # 더미의 다음을 현재 노드로 연결
	current = temp # 현재 노드를 다음 노드로 이동

# 뒤집힌 리스트 출력
reversed_list = dummy.next 
while reversed_list:
	print(reversed_list.val)
	reversed_list = reversed_list.next
```

## Double Linked List

![Untitled](https://lamarr.dev/images/algorithm/linkedlist02.jpg)

## Circular Singly Linked List

![Untitled](https://lamarr.dev/images/algorithm/linkedlist03.jpg)

## Circular Doubly Linked List

![Untitled](https://lamarr.dev/images/algorithm/linkedlist04.jpg)

## Circular Doubly Linked List
# Recerence
https://lamarr.dev/datastructure/2020/04/02/01-linked-list.html