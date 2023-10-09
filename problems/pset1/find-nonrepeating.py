#==========================================PROBLEM==========================================
# You are given a list of integers where every number appears twice EXCEPT for one of them.
# Find this number and return it from the function
# Bonus points if you can do it in linear time complexity (if you don't know what this means don't worry about it)

#Your solution should work for ANY possible array of integers
#some example testcases are given below

#=================================WRITE YOUR ANSWER BELOW==================================
def singleNumber(nums):
    # O(n), maybe a bit harder to understand though
    answer = 0
    for num in nums:
        answer = answer ^ num
    # Above uses the bitwise XOR (pronounced "X"-or) operator 
    # Let's imagine there's two variables, with binary representations as follows:
    # 1001 ^ 0101 = 1100 
    # now see: 1100 ^ 0101 = 1001 (the original value)
    return answer

def singleNumberSuboptimal(nums):
    # Mostly optimal method
    # - average case O(n) but worst case O(n^2)
    table = {}
    # [1, 4, 5, 1, 4]
    # { 1: 2, 4: 2, 5: 1}
    for n in nums:
        if n in table: # The possible problem
            table[n] += 1
        else:
            table[n] = 1

    for k,v in table.items():
        if v == 1:
            return k

    return None

def nestedSolution(nums):
    for i in nums:
        count = 0
        for j in nums:
            # Count 
            if j == i:
                count += 1
        if count == 1:
            return i


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
