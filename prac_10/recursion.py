"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
"""
Prediction:
1 + 0 + 1 + 0 + 1 then final as 0
or 3, 0

Result:
3
"""


# TODO: 2. use the debugger to step through and see what's actually happening
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)


# TODO: 3. write down what you think the output of do_something(4) will be,
"""
Prediction:
Will crash as it will run for infinity
Result:
Crashed from recursion error: depth exceeded
"""


# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)


# TODO: 5. fix do_something() so that it works according to the docstring
def do_something_better(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something_better(n - 1)


# do_something_better(4)

def do_something_better_but_backwards(n):
    numbers = []
    if n < 0:
        return
    numbers.append(n ** 2)
    do_something_better_but_backwards(n - 1)
    print(numbers[0])


# do_something_better_but_backwards(4)
def get_pyramid_blocks(n):
    if n <= 0:
        return 0
    return n + get_pyramid_blocks(n - 1)


print(get_pyramid_blocks(6))
