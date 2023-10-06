#==========================================PROBLEM==========================================
# You are given a list of integers where every number appears twice EXCEPT for one of them.
# Find this number and return it from the function
# Bonus points if you can do it in linear time complexity (if you don't know what this means don't worry about it)

#Example 1:
#   input: nums = [2,2,1]
#   output: 1
# Explanation: 1 is the only number in the array that only appears once

#Example 2:
#   input: nums = [4,1,2,1,2]
#   output: 4

#Your solution should work for ANY possible array of integers
#some example testcases are given below

#=================================WRITE YOUR ANSWER BELOW==================================
def singleNumber(nums):
    # O(n), maybe a bit harder to understand though
    ans = 0
    for n in nums:
        ans ^= n
    return ans

def singleNumberSuboptimal(nums):
    # Mostly optimal method
    # - average case O(n) but worst case O(n^2)
    table = {}
    for n in nums:
        if n in table:
            table[n] += 1
        else:
            table[n] = 1

    for k,v in table.items():
        if v == 1:
            return k

    return None



#========================================TEST CASES========================================
testcase1 = [2,2,1]
#Expeceted solution: 1
testcase2 = [4,1,2,1,2]
#Expeceted solution: 4
testcase3 = [5, 4, 3, 2, 1, 2, 3, 4, 5]
#Expeceted solution: 1

print(singleNumber(testcase1))
print(singleNumber(testcase2))
print(singleNumber(testcase3))
