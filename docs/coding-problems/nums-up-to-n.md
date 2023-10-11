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
As shown in the code snippet above, the solution simply involves creating a [python `range` object][reference: range] from __0__ to __n + 1__, then converting the object to a `list`. __n + 1__ is used as opposed to simply __n__ because this version of the range constructor will only return numbers 0 to `end` or the parameter passed in, or $$[0, n + 1)$$ in math notation.

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
Just like the previous problem, `range(0, n + 1, 2)` is used, getting a range object filled with even numbers $$[0, n)$$. This time, we need to filter out every number in this range that is a multiple of __4__. In other, more applicable terms: every value for which __value % 4 == 0__[^1] should be discarded. To do this, I used [list comprehension][reference: list comprehension], a kind of shorthand for-loop syntax that can return a list of values __if__ they meet a specified condition. If needed, under the dropdown below is an example that does not use list comprehension that may give a more clear representation of what is happening.

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
    return n
```


## Problem 5
> *Return every number in the fibonacci sequence from 0 to n*

```python
def problem5(n):
    return n
```

## Problem 6
> *Return the "nth" value of the fibonacci sequence*

```python
def problem6(n):
    return n
```

## Problem 7
> *Return ANY array containing n unique integers that add up to 0*

```python
def problem7(n):
    return n
```

___
#### Key Terms and Definitions
Function Signature
: The ...

[^1]: The modulus operator, in this example, returns the remainder of `value / 4`. To check if `value` is *not* a multiple of 4, we do *not* want the remainder to be __0__. For a basic explanation of a few modulus use cases, see this [Stack Overflow Answer][reference: basic modulus].

[python functions docs]: https://docs.python.org/3.12/library/functions.html
[reference: range]: https://docs.python.org/3/library/stdtypes.html#typesseq-range
[reference: list comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[reference: advanced prime usages]: https://www.ijsr.net/archive/v4i9/SUB157937.pdf
[reference: basic modulus]: https://stackoverflow.com/a/2609414