"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> int:
    """Detecting if a number is Armstrong number. Number must be a natural."""
    counter = 0

    def find_digits_number(num: int) -> int:
        """Calculating quantity of number's digits."""
        num //= 10
        nonlocal counter
        counter += 1
        return find_digits_number(num) if num else counter

    number_of_digits = find_digits_number(number)
    digits = (number % (10 ** x * 10) // (10 ** x) for x in range(number_of_digits))
    expected = sum(digit ** number_of_digits for digit in digits)
    return number == expected


def is_armstrong_string_solution(number: int) -> bool:
    """Detecting if a number is Armstrong number. Number must be a natural.
    Not so good but short version of solution."""
    digits = map(int, (char for char in str(number)))
    result = sum(digit ** len(str(number)) for digit in digits)
    return result == number


assert is_armstrong(153) is True, "Is Armstrong number"
assert is_armstrong(10) is False, "Is not Armstrong number"
