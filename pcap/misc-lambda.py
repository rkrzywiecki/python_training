from typing import Callable
l: Callable[[int, int], int] = lambda a, b:  a + b

print(l(2, 2))
print(l(2.0, 3.0))


def apply_func(elements: list[int], func: Callable[[int, int], int]):
    for element in elements:
        print(func(element, element))


apply_func([1,2,3,4], l)


def apply_func2(elements: list[int], func):
    for element in elements:
        print(func(element))


apply_func2([1,2,3,4], lambda x: x * x)