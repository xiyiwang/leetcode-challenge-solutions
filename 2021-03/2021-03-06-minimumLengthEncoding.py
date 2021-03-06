# LeetCode Challenge: Short Encoding of Words (2021-03-06)

#   A valid encoding of an array of words is any reference 
#   string s and array of indices indices such that:
#   - words.length == indices.length
#   - The reference string s ends with the '#' character.
#   - For each index indices[i], the substring of s starting 
#     from indices[i] and up to (but not including) the next 
#     '#' character is equal to words[i]. 
# 
#   Given an array of words, return the length of the shortest 
#   reference string s possible of any valid encoding of words.
# 
#   Constraints:
#   - 1 <= words.length <= 2000
#   - 1 <= words[i].length <= 7
#   - words[i] consists of only lowercase letters.

# Dumb & slow solution: 228 ms (faster than 26.74%)
def minimumLengthEncoding(words):
    ans = ""
    for word in sorted(list(set(words)), key=lambda w: len(w), reverse=True):
        if word + "#" not in ans:
            ans += word + "#"
    return len(ans)

# Official Solution: Store Prefixes - 116 ms
def minimumLengthEncoding2(words):
    good = set(words)
    for word in words:
        for k in range(1, len(word)):
            good.discard(word[k:])
    return sum(len(word) + 1 for word in good)
