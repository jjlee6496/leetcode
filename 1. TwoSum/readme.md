# 문제
주어진 리스트에서 서로 다른 두 원소를 더해 target 값이 나오는 두 인덱스를 순서대로 리스트로 반환
## Example 1:

Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
## Example 2:

Input: nums = [3,2,4], target = 6  
Output: [1,2]  
## Example 3:

Input: nums = [3,3], target = 6  
Output: [0,1]  

# 처음 시도
* 처음에는 브루트 포스로 같은 인덱스 일때만 거르고 모두 더해보면서 구하려고 함.
* 시간 초과, 해시맵을 사용한 방법이 있다고 함

```python
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

```
* 인덱스를 활용하여 딕셔너리에 target값 까지 부족한 값을 key, 인덱스를 value로 넣어줌
* nums를 순회하면서 나머지 수가 발견되면 먼저 저장된 인덱스와 나머지 수의 인덱스 반환