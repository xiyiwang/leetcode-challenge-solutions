"""
LeetCode Challenge: Advantage Shuffle (2021-03-24)

Given two arrays A and B of equal size, the advantage 
of A with respect to B is the number of indices i for 
which A[i] > B[i].

Return any permutation of A that maximizes its advantage 
with respect to B.

Note:
- 1 <= A.length = B.length <= 10000
- 0 <= A[i] <= 10^9
- 0 <= B[i] <= 10^9
"""
# greedy: runtime - 352 ms (faster than 72.66%)
def advantageCount(A, B):
    A_sorted, B_sorted = sorted(A), sorted(B)
    BA_map = {b: [] for b in B}
    queue = []
    j = 0

    for a in A_sorted:
        if a <= B_sorted[j]:
            queue.append(a)
        else:
            BA_map[B_sorted[j]].append(a)
            j += 1

    return [BA_map[b].pop() if BA_map[b] else queue.pop() for b in B]
    