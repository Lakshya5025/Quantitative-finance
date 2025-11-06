#Two sum

# def twoSum(self, nums: List[int], target: int) -> List[int]:
#         mp = {}
#         for i in range(0, len(nums)):
#             n = nums[i]
#             rem = target - n
#             if(mp.get(rem) != None): return [mp.get(rem), i]
#             mp[n] = i
#         return []



# Palindrome

# def isPalindrome(self, x: int) -> bool:
#         re = 0
#         temp = x
#         if(x < 0): return False
#         while(temp > 0):
#             re = re * 10 + (temp % 10)
#             temp //= 10
#         return x == re


# FizzBuzz

#  def fizzBuzz(self, n: int) -> List[str]:
#         ans = []
#         for i in range(1, n + 1):
#             if(i % 3 == 0 and i % 5 == 0): ans.append("FizzBuzz")
#             elif(i % 3 == 0): ans.append("Fizz")
#             elif(i % 5 == 0): ans.append("Buzz")
#             else: ans.append(str(i))
#         return ans
        