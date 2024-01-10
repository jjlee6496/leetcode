# 문제
문자열에서 가장 긴 팰린드롬수를 반환한다

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        max_length = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            max_length = max(len1, len2)
            if max_length > end-start:
                start = i - (max_length-1)//2
                end = i + max_length//2
        return s[start:end+1]
    def expand(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return right - left -1
```
1. 홀수 짝수의 팰린드롬 문자열을 고려, left right를 비교해서 같으면 계속 양쪽으로 뻗어나감
-> 길이 반환
2. 반복문 안에서 홀수나 짝수 팰린드롬 길이 비교후 더 긴거 가져오기
3. start end를 중앙기준으로 max_length로 복원