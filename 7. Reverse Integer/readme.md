# 문제
signed 32-bit integer range [-2^31, 2^31 - 1] 범위 내의 integer가 들어오면 거꾸로 뒤집고 범위 밖인 경우 0을 출력
```text
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
```

# 풀이
## 처음 풀이
```python
class Solution:
    def reverse(self, x: int) -> int:
        min_num, max_num = -2**31, 2**31-1
        reversed_num = int(str(x)[::-1]) if x>0 else -1*int(str(-1*x)[::-1])
        return reversed_num if min_num<=reversed_num<=max_num
```
* 문자열을 활용해서 거꾸로 뒤집기(음수일땐 절댓값으로) 그다음 다시 부호 돌려주기
* 범위에 들어가지 않으면 0 반환

## 다른 풀이
* 10진법을 사용하여 푸는 방법
```python
class Solution:
    def reverse(self, x: int) -> int:
        min_num, max_num = -2**31, 2**31-1
        reversed_num = 0
        is_negative = x<0
        if is_negative:
            x = -x
        while x != 0:
            digit = x%10
            if reversed_num>(max_num-digit):
                return 0
            reversed_num = reversed_num*10 + digit
            x //= 10
        if is_negative:
            reversed_num = -1 * reversed_num
        
        if min_num<=reversed_num<=max_num:
            return reversed_num
        else:
            return 0
```
* 시간을 줄여보기 위해 reversed_num>(max_num-digit) 조건으로 중간에 max_num을 넘어서면 return 하도록 해봤지만 문자열로 하는게 좀더 빨랐다(공간복잡도도 좀더 좋음)