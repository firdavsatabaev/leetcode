# Insert Square numbers from 1 to 10 in each index
x = []
for i in range(9):
    y = i*i
    x.append(y)
print(x)

# Pick Even numbers and return them in a list:

emptyList = []
def myfunc (*args):
    for x in args:
        if x % 2 == 0:
            emptyList.append(x)
        else:
            pass
    return emptyList
print(myfunc(5,6,7,8))


def upperString(string):
    res = []
    for letter in range(len(string)):
        if (letter+1)%2==0:
            res.append(string[letter].upper())
        else:
            res.append(string[letter].lower())
    return ''.join(res)
    
        
print(upperString("firdavs"))


# Q20: Valid Parenthesis

# stack = []
        
#         CloseToOpen = {")":"(", "]":"[", "}":"{" }
        
#         for c in s:
#             if c in CloseToOpen:
#                 if stack and stack[-1] == CloseToOpen[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         return True if not stack else False


# Question 217: COntains Duplicate

#    hashset = set()
        
#         for x in nums:
#             if x in hashset:
#                 return True
#             hashset.add(x)
#         return False


    # def twoSum(self, nums, target):
        
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
        
    #     hashmap = {}
        
    #     for index, val in enumerate(nums):
    #         diff = target - val
    #         if diff in hashmap:
    #             return[hashmap[diff], index]
    #         hashmap[val] = index
    #     return
    
    
    
# string = "gninraeL tol a nIdeknil"[::-1]
# stack = []

# for x in range(len(string)):
#     stack.append(string[x])
# print(''.join(stack))
