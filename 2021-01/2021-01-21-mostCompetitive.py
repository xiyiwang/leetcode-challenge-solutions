# LeetCode Challenge: Find the most competitive subsequence (01/21/2021)

def mostCompetitive(nums: [int], k: int) -> [int]:
    res = [None] * k
    n = len(nums)
    idx = 0
    for i, x in enumerate(nums):
        while idx != 0 and x < res[idx - 1] and idx + n - i - 1 >= k:
            idx -= 1
        if idx < k:
            res[idx] = x
            idx += 1
    return res
