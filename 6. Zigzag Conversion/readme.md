# 문제
주어진 문자열과 rowNums에 따라 지그재그로 배치하고 이를 행별로 읽었을 때 결과를 반환
```text
Example 1:

Input: s="PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

```

# 풀이
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 :
            return s
        result = ['']*numRows
        index=0
        step=0
        for char in s:
            result[index] += char
            if index==0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return ''.join(result)

```
* numRows=3을 예로 들면,
* numRows가 1이면 그대로 반환
* numRows만큼 행에 빈 문자열 추가
* index와 step 설정 각각 위치와 방향을 뜻함
* 인덱스가 0일 경우에 방향을 순방향으로 설정해줌 0행->1행->2행 순서대로 문자열이 채워짐
* 2행에 채운 후 step은 역방향으로 바뀌면서 1행->0행 순서대로 문자가 채워짐
* 이터레이티브 하게 행별로 문자열을 합쳐주면 완성