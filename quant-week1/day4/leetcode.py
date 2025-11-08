
# - ✅ Valid Anagram


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if(len(s) != len(t)): return False
#         pair = {}
#         for a in s:
#             if(pair.get(a) != None): pair[a] += 1
#             else: pair[a] = 1
#         for a in t:
#             if(pair.get(a) == None or pair.get(a) == 0): return False
#             else: pair[a] -= 1
#         return True



# - ✅ First Unique Character in a String


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         occ = {}
#         length = len(s)
#         for i in range(length):
#             ch = s[i]
#             if(occ.get(ch) != None): occ[ch].append(i)
#             else: occ[ch] = [i]
        
#         for ch in s:
#             if(len(occ[ch]) == 1): return occ[ch][0]
#         return -1

        