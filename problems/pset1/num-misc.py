#This problem has multiple steps of increasing difficulty. Complete as many as you can

#This is the value that will be passed to each function
num = 100


#PROBLEM 1: return a list of every number from 0 to n
#Ex: n = 10
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def problem1(n):
    return range(n + 1)

#PROBLEM 2: return every even number from 0 to n
def problem2(n):
    return range(0, n + 1, 2)

#PROBLEM 3: return every even number from 0 to n, NOT including multiples of 4
def problem3(n):
    return [e for e in range(0, n + 1, 2) if e % 4 != 0]

#PROBLEM 4: return every prime number from 1 to n
def problem4(n):
    # O(n^2)
    # Can definitely be otimized with some smart math, 
    # but I don't feel like thinking about it
    answer = range(1, n + 1)

    answer = [e for e in answer for f in answer if e % f != 0]

    return answer

#PROBLEM 5: return every number in the fibonacci sequence from 0 to n
def problem5(n):
    answer = []
    #Your code here

    return answer

#recursively find nth value of the fibonacci sequence
#(this function should only return 1 value, not a list)
#WARNING: Entering a number larger than 30 may take a very long time to calculate
#Bonus points if you can make it calculate the 100th number in less than a second (hint: Memoization)
def problem6(n, saved={}):
    val = 0
    if n in saved:
        return saved[n]

    if n <= 2:
        val = 1
    else:
        val = problem6(n - 1, saved) + problem6(n - 2, saved)

    saved[n] = val
    return val

#PROBLEM 7: return ANY array containing n unique integers that add up to 0
#Ex: n = 5
#output: [-7,-1,1,3,4]
#the arrays [-5,-1,1,2,3] and [-3,-1,2,-2,4] would also be accepted
#the array [0, 0, 0, 0, 0] would not be accepted because the values aren't unique
def problem7(n):
    answer = list(range(-n // 2 + 1, 0)) + list(range(1, n // 2))

    if len(answer) < n:
        answer += [0];

    return answer



print("Problem 1: ", problem1(num))
print("-Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\n")

print("Problem 2: ", problem2(num))
print("-Expected: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n")

print("Problem 3: ", problem3(num))
print("-Expected: [2, 6, 10, 14, 18]\n")

print("Problem 4: ", problem4(num))
print("-Expected: [2, 3, 5, 7, 11, 13, 17, 19]\n")

print("Problem 5: ", problem5(num))
print("-Expected: [1, 1, 2, 3, 5, 8, 13]\n")

print("Problem 6: ", problem6(num))
print("-Expected: 6765\n")

print("Problem 7: ", problem7(num))
print("List sum: ", sum(problem7(num)))
print("Expected: 0")
