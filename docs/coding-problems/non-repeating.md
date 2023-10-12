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
As always, I encourage you to try understanding this implementation on your own before proceeding. That said, here's a detailed line-by-line explanation of the code's functionality:

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
First and foremost, *just what are* bitwise operators? If you've taken any introductory computer science class (or are taking one right now), chances are that your professor, or the class textbook, has introduced the concept of bitwise operators. For a quick refresher, bitwise operators act __directly on the binary data of a value__. Here's a [good article][binary and bitwise] on how python stores integers in binary, and the basics of bitwise operators, if you need it. For this solution, we'll only be using the XOR operator, which I'll explain in more depth.
#### Properties of XOR:
The XOR operator is commonly the `^` symbol in programming, or $$\oplus$$ in mathematical notation. From now on, I will be exclusively using `^` to refer to the operator, since that's how it's used in both C++ and Python.

In this section, I'll be showing how XOR can be used to optimize the solution to this problem. But first, we must understand what it does, and how it's properties may apply. 

A quick primer on XOR: It's a bitwise operator that returns __0__ if both arguments are the same, and __1__ otherwise. Below is a table showing this relationship (where __a__ and __b__ are binary values):

|__a__|__b__|__a ^ b__|
| --- | --- | ------- |
|  0  |  0  |    0    |
|  0  |  1  |    1    |
|  1  |  0  |    1    |
|  1  |  1  |    0    |

 Looking past the definition, *behaviors* of XOR when used on more than 2 values are important to realize. The great thing about them is that they also apply to *sets of bits*; this means they will hold true for any data represented by your computer in binary *(i.e. an integer)*. The properties can be explicitly proven using *case analysis*[^4], but I'll leave that to the reader, as this explanation is already long enough. Here's a [resource][xor properties] if you're interested in looking into this further, though it may require some familiarity with the syntax of boolean algebra.
 : Commutativity: __a ^ b = b ^ a__
<!--- : Associativity: __(a ^ b) ^ c = a ^ (b ^ c) = a ^ b ^ c__ --->
 : Canceling out like terms: __a ^ a ^ b = b__ (This is the most important one for us)

Considering the implications of these two properties and the problem at hand, you may be able to see where this is leading. To recap, we want to return the singular *unique* value in a list, where all other values appear __2 times__. Below is my solution using the XOR operator. If it still doesn't make any sense, don't worry! I'll do my best to walk through the code in a step-by-step fashion, explaining how it would function with an example test case.
```python
result = 0
for num in nums:
    result ^= num
return result
```
As you can see, this solution is much smaller than (1) and (2). It iterates through the list, continuously changing `result` based on the current element. If this code looks familiar, that's because it's of the same form of how you might sum all the elements in a list. The summation would be done with `+=` rather than `^=` of course, but it's helpful to think about the similarities, as many of the same properties still apply. For instance, in taking the summation of an array, it's easier to think about it as a large addition problem, rather than an iterative loop. Here's what I mean:

- Summation of array: `[4,1,2,1,2]` => `4 + 1 + 2 + 1 + 4`
- XOR application to each element: `[4,1,2,1,2]` => `4 ^ 1 ^ 2 ^ 1 ^ 4`

Now that we've established that my code is equivalent to applying the XOR operation to each element in sequence, we can begin to use the properties of XOR that have been shown. We will first apply the property of __commutativity__ (order is irrelevant) to rearrange the equation.

`[4,1,2,1,2]` => `4 ^ 1 ^ 2 ^ 1 ^ 4` __=> `4 ^ 4 ^ 1 ^ 1 ^ 2`__

Ok, how does this help? Well, proceeding to apply our second property of the XOR operator, __canceling out like terms__, on top of this one, we can see that:

`. . .` => `4 ^ 4 ^ 1 ^ 1 ^ 2` __=> `2`__

Since the two 4's and 1's cancel out with each other. You may be able to see that this will work for *any* possible test case for the given problem. If not, here's a quick proof:

__*Let*__:  "$$n_1, n_2, \cdots, n_i$$" be the repeating elements of the given list `nums` and $$v$$ be the non-repeating element.
1. `nums` exists, by definition, as some permutation of $$v$$ and $$n_1, n_2, \cdots, n_i$$ where each $$n_i$$ appears twice and $$v$$ appears once
2. Using the property of __commutativity__ for XOR, we can deduce that computing the operation on every element in sequence can be rearranged in any way.
3. By (2), we rearrange the elements so that all repeating elements ($$n_i$$) are placed in juxtaposition to each other. Thusly, the result of XOR on all elements of `nums` becomes $$n_1 \ \hat{} \  n_1 \ \hat{} \ n_2 \ \hat{} \ n_2 \ \hat{} \ \cdots \ \hat{} \ n_i \ \hat{} \ n_i \ \hat{} \ v$$.
4. Using the property of __canceling out like terms__[^5], we can reduce the equation by removing all repeat appearances. In this case, removing all $$n_i$$. This leaves us with $$v$$, the desired result. $$\square$$

I hope my explanation was sufficient in giving you a decent understanding of how this algorithm works, or, failing that, I hope you at least gained some insight or understanding that you didn't have before. The concepts I presented are, from my experience, extremely important in the field of computer science. While you may not often use bitwise operators directly, they are essential to understand, as they control all of the underlying logic behind modern computers. I tried to introduce some semi-formal math, perhaps a bit unnecessarily, to prove the legitimacy of this final algorithm. The reason for this was to introduce the strong intermingling of math and computer science in any non-trivial problem. Don't worry if comprehension doesn't come easy, you'll eventually get closer to these problems in later computer science and math courses, as the concepts in this solution are directly related to what you'll learn in those classes.

##### Efficiency:
Time Complexity: __O(n)__ \| __Linear__

Space Complexity: __O(1)__ \| __Constant__

___
#### Key Terms and Definitions
> Iterate
: Run a block of code on each element of a given data structure, in a predetermined order (ex. a list).

> Element
: A value in a data structure, commonly an array, or *list* in python
: Ex: In the list `[1, 2, 3]` the values *1*, *2*, and *3* are *elements*.

> Optimize
: To reduce the time and/or space complexity of an algorithm

## Closing Words
Well, that's it for this problem. If you're able to understand everything I've said above then, first of all, great job. I wrote this while sleep deprived, trying to ride a caffeine-high, so it may have ended up a little less cohesive than I'd have liked. Secondly, and more importantly, it illustrates your skill in understanding a combination mathematical and computational problems. I'm aware that I left a few important concepts out, so I'm hopefully planning on publishing some subsequent pages regarding some topics. The first, and most blatant concept I left out was the meaning of time/space complexities, which I'm in the process of writing about (should be posted by Friday). I hope I wasn't overly verbose, but I'm aware that there's a disparity in the experience of many of this club's members, so I wanted to cover all possible bases. If you have any questions, suggestions, or comments, feel free to send me a message __@Matt__ on the club's discord server, or dm me. I'd greatly appreciate any feedback you're willing to give!

___
[^1]: Problem stated as given by *__@Spec__*.
[^2]: These type of algorithms are often referred to as the "naive approach" in comp sci and math. This simply means that the solution is the most apparent and the first attempt one may take. It does not necessarily imply that the solution is trivial or "bad." 
[^3]: *Well... __very__ small contingency that may make it quadratic, but it's virtual impossible with real-world numbers.*
[^4]: __*Case analysis*__ means to consider every possible *case* or *"state"* that the equation could take. Since each variable in these expressions is binary (only __0__ or __1__), you simply need to consider the set of permutations that encapsulate all possible values of __a__ and __b__ (and __c__ if it exists). It's just like the table above, except with the __"a ^ b"__ column changed to whatever the equation is.
[^5]: *Totally* a mathematically proper name. Sorry, I was tired...
[python dict]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[binary and bitwise]: https://wiki.python.org/moin/BitwiseOperators
[xor properties]: https://markusthill.github.io/electronics/a-few-properties-of-the-exclusive-or/