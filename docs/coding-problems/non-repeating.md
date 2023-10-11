# Problem Solution and Explanation: Find the Non-Repeating Integer
In the following page, I will outline 3 distinct solutions to the aforementioned problem, beginning with the most intuitive and ending with one slightly more challenging.
## The Problem:
We are given a list of integers where every number appears twice EXCEPT for one of them.[^1] Some examples of input, along with their desired outputs, are below.

`[2,2,1] => 1` `[4,1,2,1,2] => 4` `[5, 4, 3, 2, 1, 2, 3, 4, 5] => 1`

In all of the following solutions, `nums` is defined as the list of integers.

## 1) "Straightforward"[^2] Solution:
Looking at this problem initially, it's clear that we need to iterate through the list *at least* once. Each pair of like elements should be found and noted, leaving the one remaining element as the result.
The first question that arises is, how do we check whether each element has a corresponding equal? One approach that may come to mind is to use *nested iteration*. That is, iterate through the list and within that loop, iterate again, checking each element for equality. If the current element has a counterpart, we can discard it and move on, as we only care about elements __without__ an equal counterpart.

Here is an implementation of this idea:
```python
for a in nums:
    appears: int = 0
    for b in nums:
        if a == b:
            appears += 1
    if appears == 1:
        return a
```
Ahead, I've written an analysis of this code line-by-line. You should first try to work through the code yourself, however, if you do not yet understand what it does.

`for a in nums:` Begins a loop to iterate through each element in the list *nums*

`→ appears: int = 0` Defines the variable *appears* of type integer, initialized at 0

`→ for b in nums:` Begins a nested loop to iterate through each element in the list *nums*. This takes place __within__ the outer loop.

`→ → if a == b:` Checks whether the value of the outer loop is the same as the inner. In context of the problem, it checks if both loops are on the same element or a repeated element.

`→ → → appears += 1` Adds 1 to *appears* denoting that an appearance of the current value has been found in the list.

`→ if appears == 1:` Checks if the value only appeared once.

`→ → return a` Returns the value of the current iteration

___
In simple and concise terms: the *number of appearances* of each value in the list will be tallied. Then, if the total tally of __any__ value is equal to 1 (i.e. the value __does not repeat__), that value is returned. That's it. No complex logic or arithmetic, just tallying the number of appearances of each value in the list.

This algorithm is by no means the most efficient approach to the problem, but it should be fairly simple to understand. The above code snippet is just one possible implementation, and there are certainly ways to take this same idea and optimize it; however, I'll be leaving that as an exercise for the reader.
##### Efficiency:
Time Complexity: __O($$\textbf{n}^\textbf{2}$$)__ \| __Quadratic__

Space Complexity: __O(1)__ \| __Constant__

## 2) Idiomatic Solution:
After spending some time trying to make previous solution more efficient, you may discover that there's not much you can do, at least not with the ideas already presented. Sure, you could skip checking the current element, or even break out of the inner loop whenever `appears == 2` but these optimizations will not reduce the algorithm's overall time complexity. To achieve this, we need to somehow remove the nested loop, iterate through the list just __one time__. Take a minute to consider what you know, and think about how this could be done. Then, read on!

The answer to the issue is to cache the elements as we go along. If we encounter an element that has not yet been seen, it is added to the cache. If we *have* already seen it (i.e. it exists in the cache), then its position in the cache is *flagged*, denoting that it occurs multiple times. This *cache* can be visualized much like a list, with each element pointing to a value, our *flag* value in this case. In python, this data structure would be best represented with the [built-in `dict` (dictionary) type][python dict]. I'll leave it to you to click the link and learn more about this structure yourself, if necessary.

After reading all this, you might have a pretty good idea of how to implement this concept in python. If not, don't worry, here's my implementation:
```python
cache = {}
for num in nums:
    if num in cache:
        cache[num] = True
    else:
        cache[num] = False

for num,flag in cache.items():
    if not flag:
        return num
```
Once again, please try to understand this implementation yourself before reading on. That being said, here's a line-by-line explanation of what's happening:

__Dictionary setup:__

`cache = {}` Sets cache to an empty *dictionary*

`for num in nums:` Begins iterating through nums

`→ if num in cache:` Checks if the current value is already cached

`→ → cache[num] = ``True`/`False` Sets the flag for the current value in the cache, based on whether it has repeated or not

__Final check:__

`for num,flag in cache.items():` Begins iterating through the cached data, using key/value pairs

`→ if not flag:` Checks if the current item does __not__ have its flag set (i.e. value does not repeat in original list)

`→ → return num` *As written*

___
Compared to the "straightforward" solution, this approach improves efficiency drastically. Using caching, it manages to decrease the time complexity by a factor of *n* (the length of the list). The concept of caching is widely used in nearly every computer application, and is versatile in solving many problems in efficiency. With this skill, you should be able to solve quite a few other basic algorithmic problems. 
<!--- Include link to said problems --->

##### Efficiency:
Time Complexity: __O(n)__ \| __Linear__[^3] 

Space Complexity: __O(n)__ \| __Linear__

## 3) Bitwise Solution:
All right! Last, but certainly not least, is a solution that may not come intuitively if you don't have a good understanding of bitwise operators, or boolean algebra. The following explanation should hopefully help amend that.
#### Bitwise Operators and Binary Data:
First and foremost, *just what are* bitwise operators? If you've taken any introductory computer science class (or are taking one right now), chances are that your professor, or the class textbook, has introduced the concept of bitwise operators. For a quick refresher, bitwise operators act __directly on the binary data of a value__. Here's a [good article][binary and bitwise] on how python stores integers in binary, and the basics of bitwise operators, if you need it. For this solution, we'll only be using the XOR operator, which I'll soon explain in more depth.
#### Properties of XOR:
The XOR operator is commonly the `^` symbol in programming, or $$\oplus$$ in mathematical notation. From now on, I will be exclusively using `^` to refer to the operator, since that's how it's used in both C++ and Python.

In this section, I'll be showing how XOR can be used to optimize the solution to this problem. But first, we must understand what it does, and how it's properties may apply. The usage of XOR is on binary data, and thusly, the truth table below shows all possible equations:

|__a__|__b__|__a ^ b__|
| --- | --- | ------- |
|  0  |  0  |    0    |
|  0  |  1  |    1    |
|  1  |  0  |    1    |
|  1  |  1  |    0    |

Where __a__ and __b__ are binary values. Looking past the definition, *behaviors* of XOR are much more important to realize.
##### Associative and Commutative Properties:

##### Efficiency:
Time Complexity: __O(n)__ \| __Linear__

Space Complexity: __O(1)__ \| __Constant__
___
#### Key Terms and Definitions
Iterate
: Run a block of code on each element of a given data structure, in a predetermined order (ex. a list).

Element
: A value in a data structure, commonly an array, or *list* in python
: Ex: In the list `[1, 2, 3]` the values *1*, *2*, and *3* are *elements*.

Optimize
: To...

___
[^1]: Problem stated as given by *__@Spec__*.
[^2]: These type of algorithms are often referred to as the "naive approach" in comp sci and math. This simply means that the solution is the most apparent and the first attempt one may take. It does not necessarily imply that the solution is trivial or "bad." 
[^3]: *Well... __very__ small contingency that may make it quadratic, but it's virtual impossible with real-world numbers.*
[python dict]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[binary storage]: 