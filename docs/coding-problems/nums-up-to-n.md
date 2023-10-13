# Problem Solution and Explanation: Numbers up to N
In the following page, I will explain the solutions for each of this problem's 7 steps. Some of these solutions are trivial, using very basic python constructs, so I may just include the code and a short explanation regarding these. If you need help in understanding exactly how these python functions work, I recommend going to [python's official documentation page][python functions docs]. I will be including more specific links for further reference as needed.

Here are links to each problem, if you'd like to jump to a specific one:
: [Problem 1](#problem-1)
: [Problem 2](#problem-2)
: [Problem 3](#problem-3)
: [Problem 4](#problem-4)
: [Problem 5](#problem-5)
: [Problem 6](#problem-6)
: [Problem 7](#problem-7)

## Problem 1
> *Return a list of every number from 0 to n*

```python
def problem1(n):
    return list(range(n + 1))
```
As shown in the code snippet above, the solution simply involves creating a [python `range` object][reference: range] from __0__ to __n + 1__, then converting the object to a `list`. __n + 1__ is used as opposed to simply __n__ because this version of the range constructor will only return numbers 0 to `end` or the parameter passed in, or $$\left[0, n + 1\right)$$ in math notation.

## Problem 2
> *Return every even number from 0 to n*

```python
def problem2(n):
    return list(range(0, n + 1, 2))
```
This problem has a very similar solution to the previous, the only difference being the usage of a different *signature* of the range function: `range(start, stop, step)`. In the above snippet, __0__, __n + 1__, and __2__ are passed to `start`, `stop`, and `step` respectively. You may notice that `start` and `stop` are passed in as the exact as in problem 1 (`start` = 0 was just implicit before). However, the setting the last parameter to __2__ ensures that each value in the returned range object will be 2 away from the previous. Since we start with __0__, it can be seen that every subsequent value will be even.

## Problem 3
> *Return every even number from 0 to n not including multiples of 4*

```python
def problem3(n):
    return [value for value in range(0, n + 1, 2) if value % 4 != 0]
```
Just like the previous problem, `range(0, n + 1, 2)` is used, getting a range object filled with even numbers $$[0, n)$$. This time, we need to filter out every number in this range that is a multiple of __4__. In other, more applicable terms: every value for which __value % 4 == 0__[^1] should be discarded. To do this, I used [list comprehension][reference: list comprehension], a kind of shorthand for-loop syntax that returns a list of values __if__ they meet a specified condition. If needed, under the dropdown below is an example that does not use list comprehension that may give a more clear representation of what is happening.

<details>
<summary>Alternative Solution</summary>
{% highlight python %}
def problem3(n):
    result = []
    for value in range(0, n + 1, 2):
        if value % 4 != 0:
            result.append(value)
    return result
{% endhighlight %}
</details>

## Problem 4
> *Return every prime number from 1 to n*

```python
def problem4(n):
    is_prime = [True] * (n + 1)

    i = 2
    while i * i <= n:
        if is_prime[i]:
            for not_p in range(i * i, n + 1, i):
                is_prime[not_p] = False
        i += 1

    result = [num for num in range(2, n + 1) if is_prime[num]]

    return result
```
#### Sieve of Eratosthenes:
Eratosthenes was a greek mathematician who devised an algorithmic method for filtering[^2] out the non-primes from a subset of natural numbers (*Natural Numbers* => $$\mathbb{N} = \{1, 2, 3, \cdots\}$$) defined by $$[0, n]$$. The algorithm consists of the following steps:
1. Begin with all Natural numbers $$[2, n]$$ marked as prime. Let $$k=2$$.
2. Mark each multiple of $$k$$, from $$k^2$$ to $$n$$, as non-prime.
3. Set $$k$$ to the next number still marked prime
4. Repeat (2) and (3) while $$k<\sqrt n$$

Let's break this down visual to understand it better. Numbers in <span style="color:green;font-weight: bold;">green</span> are currently marked as prime, and non-primes are unmarked.

___

01|<span style="color:green;font-weight: bold;">02|<span style="color:green;font-weight: bold;">03|<span style="color:green;font-weight: bold;">04|<span style="color:green;font-weight: bold;">05|<span style="color:green;font-weight: bold;">06|<span style="color:green;font-weight: bold;">07|<span style="color:green;font-weight: bold;">08|<span style="color:green;font-weight: bold;">09|<span style="color:green;font-weight: bold;">10
<span style="color:green;font-weight: bold;">11|<span style="color:green;font-weight: bold;">12|<span style="color:green;font-weight: bold;">13|<span style="color:green;font-weight: bold;">14|<span style="color:green;font-weight: bold;">15|<span style="color:green;font-weight: bold;">16|<span style="color:green;font-weight: bold;">17|<span style="color:green;font-weight: bold;">18|<span style="color:green;font-weight: bold;">19|<span style="color:green;font-weight: bold;">20
<span style="color:green;font-weight: bold;">21|<span style="color:green;font-weight: bold;">22|<span style="color:green;font-weight: bold;">23|<span style="color:green;font-weight: bold;">24|<span style="color:green;font-weight: bold;">25|<span style="color:green;font-weight: bold;">26|<span style="color:green;font-weight: bold;">27|<span style="color:green;font-weight: bold;">28|<span style="color:green;font-weight: bold;">29|<span style="color:green;font-weight: bold;">30
<span style="color:green;font-weight: bold;">31|<span style="color:green;font-weight: bold;">32|<span style="color:green;font-weight: bold;">33|<span style="color:green;font-weight: bold;">34|<span style="color:green;font-weight: bold;">35|<span style="color:green;font-weight: bold;">36|<span style="color:green;font-weight: bold;">37|<span style="color:green;font-weight: bold;">38|<span style="color:green;font-weight: bold;">39|<span style="color:green;font-weight: bold;">40
<span style="color:green;font-weight: bold;">41|<span style="color:green;font-weight: bold;">42|<span style="color:green;font-weight: bold;">43|<span style="color:green;font-weight: bold;">44|<span style="color:green;font-weight: bold;">45|<span style="color:green;font-weight: bold;">46|<span style="color:green;font-weight: bold;">47|<span style="color:green;font-weight: bold;">48|<span style="color:green;font-weight: bold;">49|<span style="color:green;font-weight: bold;">50

As outlined by step (1) of the algorithm, all numbers $$[2, n]$$ are marked as prime, with $$n=50$$ here.

01|<span style="color:green;font-weight: bold;">02|<span style="color:green;font-weight: bold;">03|04|<span style="color:green;font-weight: bold;">05|06|<span style="color:green;font-weight: bold;">07|08|<span style="color:green;font-weight: bold;">09|10
<span style="color:green;font-weight: bold;">11|12|<span style="color:green;font-weight: bold;">13|14|<span style="color:green;font-weight: bold;">15|16|<span style="color:green;font-weight: bold;">17|18|<span style="color:green;font-weight: bold;">19|20
<span style="color:green;font-weight: bold;">21|22|<span style="color:green;font-weight: bold;">23|24|<span style="color:green;font-weight: bold;">25|26|<span style="color:green;font-weight: bold;">27|28|<span style="color:green;font-weight: bold;">29|30
<span style="color:green;font-weight: bold;">31|32|<span style="color:green;font-weight: bold;">33|34|<span style="color:green;font-weight: bold;">35|36|<span style="color:green;font-weight: bold;">37|38|<span style="color:green;font-weight: bold;">39|40
<span style="color:green;font-weight: bold;">41|42|<span style="color:green;font-weight: bold;">43|44|<span style="color:green;font-weight: bold;">45|46|<span style="color:green;font-weight: bold;">47|48|<span style="color:green;font-weight: bold;">49|50

Going to step (2), we take every multiple of **2**, beginning with $$2^2$$, or **4**, up to $$n=50$$ and mark them all as non-prime.

01|<span style="color:green;font-weight: bold;">02|<span style="color:green;font-weight: bold;">03|04|<span style="color:green;font-weight: bold;">05|06|<span style="color:green;font-weight: bold;">07|08|09|10
<span style="color:green;font-weight: bold;">11|12|<span style="color:green;font-weight: bold;">13|14|15|16|<span style="color:green;font-weight: bold;">17|18|<span style="color:green;font-weight: bold;">19|20
21|22|<span style="color:green;font-weight: bold;">23|24|<span style="color:green;font-weight: bold;">25|26|27|28|<span style="color:green;font-weight: bold;">29|30
<span style="color:green;font-weight: bold;">31|32|33|34|<span style="color:green;font-weight: bold;">35|36|<span style="color:green;font-weight: bold;">37|38|39|40
<span style="color:green;font-weight: bold;">41|42|<span style="color:green;font-weight: bold;">43|44|45|46|<span style="color:green;font-weight: bold;">47|48|<span style="color:green;font-weight: bold;">49|50

Then, we choose the next prime $$k$$ value, **3** in this case, and since $$k\lt{\sqrt{n}}$$ ($$3\lt{\sqrt{50}}$$), we go back to step (2) and mark all multiples of **3**, beginning with **9** as non-prime.

01|<span style="color:green;font-weight: bold;">02|<span style="color:green;font-weight: bold;">03|04|<span style="color:green;font-weight: bold;">05|06|<span style="color:green;font-weight: bold;">07|08|09|10
<span style="color:green;font-weight: bold;">11|12|<span style="color:green;font-weight: bold;">13|14|15|16|<span style="color:green;font-weight: bold;">17|18|<span style="color:green;font-weight: bold;">19|20
21|22|<span style="color:green;font-weight: bold;">23|24|25|26|27|28|<span style="color:green;font-weight: bold;">29|30
<span style="color:green;font-weight: bold;">31|32|33|34|35|36|<span style="color:green;font-weight: bold;">37|38|39|40
<span style="color:green;font-weight: bold;">41|42|<span style="color:green;font-weight: bold;">43|44|45|46|<span style="color:green;font-weight: bold;">47|48|49|50

We do subsequent passes just like those before with the numbers **5** and **7**, and at that point, the next prime number (**11**) is greater than $$\sqrt{50}\approx{7.07}$$. Consequently, the algorithm ends and we are left with a set of correctly marked prime numbers as seen above.

___
If you look back to my python implementation of the sieve, you may see how it's steps directly mirror my description of the algorithm above. First, I initialize an list of boolean values of size `n + 1` to include all numbers from $$[0, n]$$. These all begin as `True` (marked as prime). Then I iterate through this list, marking any composite numbers as *non-prime*, in the same way as outlined above. Note that the conditional of the `while` loop, `i * i <= n` is equivalent to $$i \le \sqrt{n}$$. Within this outer loop, I check if the current number is marked as prime. If so, I iterate through all of its factors in $$\left[i^2, n\right]$$, marking them as composite. After these nested loops finish, I am left with a boolean list of size **n + 1**, with all primes marked as `True` and all composites marked as `False`. All that is left is to iterate through this list one last time, and translate it into a new list containing only prime numbers. This is done with list comprehension, with `result = . . .`. Starting at **2** and going to **n + 1**, checking if each corresponding value in `is_prime` is `True`, and adding that number to the list if so.

<!--- Other prime naive solution --->

## Problem 5
> *Return every number in the fibonacci sequence from 0 to n*

```python
def problem5(n):
    result = []
    
    previous, current = 0, 1
    while current < n:
        result.append(current)
        next_val = current + previous
        previous = current
        current = next_val

    return result
```
This one's not too complex, so I'll just do a line-by-line explanation:

`result = []` Create an empty list. This will be the variable returned

`prev, current = 0, 1` Initialize two variables, `previous` and `current`, to **0** and **1** respectively. `previous` will hold the value of the prior value in the sequence while `current` will hold the value used in the running iteration, hence the names

`while current < n:` Since we want every number in the sequence from $$\left[0, n\right)$$, we simply iterate until `current >= n`

`result.append(current)` Add `current` to the result

`next_val = current + previous` This is a new variable that will hold the value of the *next iteration's* `current`. It is needed here, since `previous` and `current` are both changed based on each other's values, which is impossible to do without intermittently storing the result somewhere.

`previous = current` Setting the `previous` for the next iteration to this one's `current`

`current = next_val` Using the value we stored, `current + previous`, we can now set the next iteration's `current`

`return result` ...

The idea of the fibonacci sequence is that each term is added to the previous, creating the next. It looks like this: `1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`. We achieve this behavior by storing the previous and current values as variables, and always setting the next *current* value to `previous + current`.

## Problem 6
> *Return the "nth" value of the fibonacci sequence*

```python
def problem6(n):
    if n <= 2:
        return 1
    
    return problem6(n - 1) + problem6(n - 2)
```
This problem is much similar to the prior, except that we only need *the final* value. The first two lines should be self-explanatory: if `n` is **1** or **2** we should return **1**, since the first two values of the fibonacci sequence are **1**. The return statement introduces the concept of recursion, or calling of a function within itself. These calls map nicely to the concept of the fibonacci sequence, because we know that each value of the each value in the sequence is equal to the sum of the prior two values. In this code, that idea is presented as `problem6(n) = problem6(n - 1) + problem6(n - 2)`. Calling function with `n = 4` would result in the following function calls:
```
problem6(4) = 2 + 1 = 3
|
|---> problem6(3) = 1 + 1 = 2
|     |
|     |---> problem6(2) = 1
|     |
|     |---> problem6(1) = 1
|
|---> problem6(2) = 1
```
The program begins at the top of the hierarchy, with `n = 4`. The function `problem6` will then call itself with arguments `n - 1` and `n - 2` or **3** and **1** in this case. Since $$1 \le{2}$$ that branch of the call stack terminates and returns **1** (the leading if statement that I explained above). **3**, however, is still greater than 2, so the function will recursively call itself twice more with `n = 2` and `n = 1`. Both of these satisfy the $$\le{2}$$ condition, so they will both terminate and return **1**. Working from the bottom to determine the result, we can see that each function one level up in the hierarchy will return the sum of the two calls below it. In this case, `problem6(3)` returns `problem6(2) + problem6(1)` or `1 + 1`. `problem6(4)`, the topmost call, will return `problem6(3) + problem6(2)` or `2 + 1`. This same idea can be extended for any positive **n** argument, where the return of that call is based on a hierarchy of functions `n - 1`, `n - 2`, `(n - 1) - 1`, `(n - 1) - 2`, etc. until all of these functions terminate when $$n\le{2}$$.

The biggest problem with this approach is its exponential time complexity, **O($$2^n$$)**. You can see already with `n = 4` that repeat function calls of `problem6(2)` are being made. This problem grows vastly when `n` is very large. The solution to this is to introduce a data structure to store prior function calls along with their results, and use them as needed. That way, the computations need only be made once. Below I have an implementation of this idea, but I urge you to try to do it yourself first. Since it's recursive, you'll need to introduce a new parameter to the function, with a default argument. The built-in `dict` type would probably work best for this, as we want to store each function call **and** its corresponding output to cache the results. Good luck!
<details>
<summary>Memoization Solution:</summary>
{% highlight python %}
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
{% endhighlight %}
</details>
Here's a great resource on the concept of [memoization][reference: memoization], involving the caching of recursive function calls (and a few more neat concepts).

## Problem 7
> *Return ANY array containing n unique integers that add up to 0*

```python
def problem7(n):
    result = list(range(-(n // 2), 0)) + list(range(1, n // 2 + 1))

    if len(result) < n:
        result += [0];

    return result
```
This code may look a bit convoluted, but what it does it quite simple. To explain briefly, it creates an array of length `n` (as specified), filled with corresponding sets of positive and negative numbers. Then, if `n` is odd, it adds on the element `[0]`; that's it. Here's some examples of what it does with different inputs of `n`:

`problem7(2) = [-1] + [1] = [-1, 1]`

`problem7(3) = [-1] + [1] + [0] = [-1, 1, 0]`

`problem7(6) = [-3, -2, -1] + [1, 2, 3] = [-3, -2, -1, 1, 2, 3]`

`problem7(7) = [-3, -2, -1] + [1, 2, 3] + [0] = [-3, -2, -1, 1, 2, 3, 0]`

Going over the simplest part first, the if statement midway through the function checks if `len(result) < n` meaning that the final list is still smaller than it needs to be, which in this case indicates that `n` is an odd number. If this is true, the element `[0]` is simply added on to the list.

Now for the first line of the function, which contains most of the logic. As you can see, I create two lists based on `range` objects. In creating these objects, I use python's `//` operator. Similar to normal division, `/`, except it always rounds down to the nearest integer. For instance, `5 // 2` will be **2**, while `-7 // 2` is **-4**. In this program, I always want the result to be rounded towards **0**, so I make sure to use `-(n // 2)` when dealing with negative numbers. These ranges basically go from `-(n / 2) to 0` and `0 to (n / 2)` respectively. The `//` operator and `+ 1` are there to ensure that they work properly when dealing with odd numbers not divisible by **2**. This is probably one of the simplest ways to do this problem, and it would be great practice to try implementing some other solution that doesn't use two mirror sets of positive and negative numbers.

___
#### Key Terms and Definitions
Function Signature
: A function's *name* and *parameters* (and in special cases its *return type* as well)

## Closing Remarks
Well, that's a wrap. I hope none of the explanations felt rushed or noncohesive, and that I didn't leave out any essential information. If you have any questions, comments, or suggestions, please feel free to contact me on discord! I really enjoyed writing this, as  it helped cement my own knowledge of some of the fundamentals.


[^1]: The modulus operator, in this example, returns the remainder of `value / 4`. To check if `value` is *not* a multiple of 4, we do *not* want the remainder to be __0__. For a basic explanation of a few modulus use cases, see this [Stack Overflow Answer][reference: basic modulus].
[^2]: or "sieving," thus the name
[python functions docs]: https://docs.python.org/3.12/library/functions.html
[reference: range]: https://docs.python.org/3/library/stdtypes.html#typesseq-range
[reference: list comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[reference: advanced prime usages]: https://www.ijsr.net/archive/v4i9/SUB157937.pdf
[reference: basic modulus]: https://stackoverflow.com/a/2609414
[reference: memoization]: https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/