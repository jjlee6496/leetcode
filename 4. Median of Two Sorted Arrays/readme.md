# 문제
주어진 두 리스트를 합쳐 median 값을 반환, 시간 복잡도 O(log(m+n))

```text
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

# 첫번째 풀이
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        nums = sorted(nums1 + nums2)
        if (m+n) % 2:
            return nums[(m+n)//2]
        else:
            return (nums[(m+n)//2-1] + nums[(m+n)//2])/2.0 # 2로 나누면 int 처리됨
```
* 풀긴 했지만 시간이 많이 듦