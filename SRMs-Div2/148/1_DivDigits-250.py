"""
Problem Statement
Create a class DivDigits containing a method howMany which takes as an argument an int number andreturns how many digits
in number that number itself is divisible by.Count all occurences of such digits in the number, not just the first. See
examples for more information.

  
Class: DivisorDigits
Method: howMany
Parameters: integer
Returns: integer
Method signature: def howMany(self, number):

Notes
-	No number is divisible by 0.

Constraints
-	number will be an int between 10000 and 999999999, inclusive (between 5 and 9 digits, inclusive).

Examples
0)
12345
Returns: 3
12345 is divisible by 1, 3, and 5.

1)
661232
Returns: 2
661232 is divisible by 1 and 2.

2)
52527
Returns: 0
52527 is not divisible by 5, 2, or 7.

3)
730000000
Returns: 0
Nothing is divisible by 0. In this case, the number is also not divisible by 7 or 3.
"""


class DivsorDigits:
    def howMany(self, number):
        num = str(number)
        count = 0
        for i in range(1, 10):
            if number % i == 0 and str(i) in num:
                count += 1

        return count
