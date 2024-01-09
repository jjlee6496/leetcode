# 문제
* 문자열 s가 주어졌을 때 같은 글자가 반복되지 않는 가장 긴 substring의 길이를 반환
```text
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

# 처음 시도
```python
from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = deque(list(s))
        length = 0
        ans = []
        while l:
            temp = l.popleft()
            if temp in ans:
                if length < len(ans):
                    length = len(ans)
                    if ans[-1] in l:
                        ans = [temp]
                    elif ans[-1] not in l:
                        ans = [ans[-1], temp]
                    else:
                        ans = []
                
            else:
                ans.append(temp)
        return length if length > len(ans) else len(ans)
```
* 처음에 사람이 읽듯이 왼쪽에서 부터 하나하나 후보군에 담아 가면서 처리하려고 했지만 예외 상황들 'dvdf'(v를 버리면 안됨 -> 3이 나와야함) 'aab'(중복이라고 버리면 안됨) 같은 케이스 들이 발생
* sliding window 기법 이라는 것이 있다고 함.
```python
def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = start = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, i - start + 1)

        char_index[char] = i

    return max_length

```
* 문자와 그 인덱스에 대해서
* 문자를 읽는 시작지점을 0으로 지정함
* 문자의 인덱스를 딕셔너리에 저장하면서 가다가 이미 존재하는 문자이고 시작지점보다 왼쪽이라면 시작지점을 바꿔준다 -> 여기서 위의 문제 해결
* max length는 시작지점 부터 1씩 늘어나면서 저장된 max length와 비교해서 더 큰값을 가져감 -> 가장 큰 substring 길이 반환