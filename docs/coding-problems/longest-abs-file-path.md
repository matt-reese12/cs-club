# Problem Solution and Explanation: Longest Absolute File Path (LeetCode)
[LeetCode Link](https://leetcode.com/problems/longest-absolute-file-path/)

### UNDER CONSTRUCTION (SORRY)

## My Initial Sub-Optimal Solution
```python
def lengthLongestPath(input: str) -> int:
    nodes = input.split('\n')
    stack = []
    maxPath = ""

    for node in nodes:
        depth = node.count('\t')

        while depth < len(stack):
            stack.pop()
        stack.append(node.strip('\t'))

        if '.' in node: # Check if it's a file
            strPath = '/'.join(stack)
            if len(strPath) > len(maxPath):
                maxPath = strPath

    return len(maxPath)
```

## Better Solution
This solution is implemented by storing path lengths rather than the paths themselves, optimizing memory usage.
```python
def lengthLongestPath(input: str) -> int:
    nodes = input.split('\n')
    stack = []
    max_length = 0

    for node in nodes:
        depth = node.count('\t')

        while depth < len(stack):
            stack.pop()
        if depth == 0:
            stack.append(len(node))
        else:
            stack.append(stack[-1] + 1 + len(node) - depth)
        
        if '.' in node:
            max_length = max(max_length, stack[-1])

    return max_length
```

Here's a pretty decent explanation [on leetcode](https://leetcode.com/problems/longest-absolute-file-path/solutions/3254721/388-time-100-solution-with-step-by-step-explanation/) of the solution.