# 문제
주어진 height 리스트에서 두개의 높이를 골라서 최대의 면적을 반환하기
![](https://github.com/jjlee6496/leetcode/blob/main/11.%20Container%20With%20Most%20Water/20240111134955.png)
# 풀이
## 처음풀이
* 브루트 포스는 O(N^2)이라 시간 초과
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i != j:
                    temp = self.area(height,i, j)
                    max_area = max(max_area, temp)
        return max_area
    def area(self, height, left, right):
        return (right-left)*min(height[left], height[right])
```

## 그리디
* 포인터를 두개 두고 움직임
* 포인터를 움직이면 거리가 줄어드는 만큼 넓이를 최대화하기 위해선 더 높은 기둥을 포함해야 함
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, h*w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
```
