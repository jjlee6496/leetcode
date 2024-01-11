# 문제
주어진 문자열이 팰린드롬 수이면 true 아니면 false를 반환
```text
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

# 풀이
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False

        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num*10 + x%10
            x //= 10

        return x == reversed_num or reversed_num//10 == x

```
* 7번문제에서 처럼 10진법으로 숫자를 뒤집음
* 0이아닌 10의 배수이거나 음수이면 팰린드롬수가 될수 없으므로 False 반환
* 12321을 예로 들면 기존숫자가 12, 뒤집은 수가 123에서 while문 멈춤
* 뒤집은 수의 10으로 나눈 몫 12==12이므로 True, 짝수길이의 수 이면 둘이 완전히 같으므로 True 반환 그렇지 않으면 False가 반환됨