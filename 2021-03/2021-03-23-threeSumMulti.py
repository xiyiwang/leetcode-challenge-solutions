"""
LeetCode Challenge: 3Sum With Multiplicity (2021-03-23)

Given an integer array arr, and an integer target, return 
the number of tuples i, j, k such that i < j < k and 
arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Constraints:
- 3 <= arr.length <= 3000
- 0 <= arr[i] <= 100
- 0 <= target <= 300
"""

# 3 pointers: time complexity - O(n^2)
def threeSumMulti(arr, target):
    MOD = 10**9 + 7
    ans = 0
    arr.sort()
    
    for p1, n1 in enumerate(arr):
        T = target - n1
        p2, p3 = p1+1, len(arr)-1

        while p2 < p3:
            if arr[p2] + arr[p3] < T:
                p2 += 1
            elif arr[p2] + arr[p3] > T:
                p3 -= 1
            else: # n2 + n3 == T
                if arr[p2] != arr[p3]:
                    l = r = 1
                    while p2 + 1 < p3 and arr[p2] == arr[p2+1]:
                        l += 1
                        p2 += 1
                    while p3 - 1 > p2 and arr[p3] == arr[p3-1]:
                        r += 1
                        p3 -= 1
                    
                    ans += l * r
                    p2 += 1
                    p3 -= 1
                else:
                    ans += (p3-p2+1) * (p3-p2) / 2
                    break

    return int(ans%MOD)
