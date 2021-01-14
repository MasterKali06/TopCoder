"""
Problem Statement
9 numbers need to be arranged in a magic number square. A magic number square is a square of numbers that is arranged
such that every row and column has the same sum. For example:

1 2 3
3 2 1
2 2 2

Create a class MNS containing a method combos which takes as an argument a int[] numbers and returns the number of
distinct ways those numbers can be arranged in a magic number square. Two magic number squares are distinct if they
differ in value at one or more positions. For example, there is only one magic number square that can be made of 9
instances of the same number.


Class: MNS
Method: combos
Parameters: tuple (integer)
Returns: integer
Method signature: def combos(self, numbers):

Notes
-	Unlike some versions of the magic number square, the numbers do not have to be unique.

Constraints
-	numbers will contain exactly 9 elements.
-	each element of numbers will be between 0 and 9, inclusive.

Examples
0)
{1,2,3,3,2,1,2,2,2}
Returns: 18

1)
{4,4,4,4,4,4,4,4,4}
Returns: 1

2)
{1,5,1,2,5,6,2,3,2}
Returns: 36

3)
{1,2,6,6,6,4,2,6,4}
Returns: 0
"""
# best readable program for this problem
from collections import Counter
from math import factorial


class MNS:
    # defining the count to keep the ways (not distinct yet)
    def __init__(self):
        self.count = 0

    # defing a permutation function
    def permute(self, a, start, end):

        if start == end:
            # looking for the magic squares (not distinct yet)
            if sum(a[0:3]) == sum(a[3:6]) == sum(a[6:9]) == a[0]+a[3]+a[6] == a[1]+a[4]+a[7] == a[2]+a[5]+a[8]:
                self.count += 1

        else:

            for i in range(start, end + 1):
                a[start], a[i] = a[i], a[start]

                self.permute(a, start + 1, end)

                a[start], a[i] = a[i], a[start]

    def combos(self, numbers):
        # listing the given tuple and pass it to permute function
        numbers = list(numbers)
        self.permute(numbers, 0, 8)

        # make a counter
        counter = Counter(numbers)

        # dividing count to factorial of the repeated values will give us distinct magic squares
        for i in counter.values():
            self.count //= factorial(i)

        return self.count

