#==========================================PROBLEM==========================================
#You are given a list of integers where every number appears twice EXCEPT for one of them.
#Find this number and return it from the function
#Bonus points if you can do it in linear time complexity (if you don't know what this means don't worry about it)

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
    answer = set(nums)

    return #answer here



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
