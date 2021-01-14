"""
Problem Statement
In documents, it is frequently necessary to write monetary amounts in a standard format.
We have decided to format amounts as follows:
    the amount must start with '$'
    the amount should have a leading '0' if and only if it is less then 1 dollar.
    the amount must end with a decimal point and exactly 2 following digits.
    the digits to the left of the decimal point must be separated into groups of three by commas
    (a group of one or two digits may appear on the left).
Create a class FormatAmt that contains a method amount that takes two int's, dollars and cents, as inputs and returns
the properly formatted String.


Class: FormatAmt
Method: amount
Parameters: integer, integer
Returns: string
Method signature: def amount(self, dollars, cents):

Notes
-	One dollar is equal to 100 cents.

Constraints
-	dollars will be between 0 and 2,000,000,000 inclusive
-	cents will be between 0 and 99 inclusive

Examples
0)
123456
0
Returns: "$123,456.00"
Note that there is no space between the $ and the first digit.

1)
49734321
9
Returns: "$49,734,321.09"

2)
0
99
Returns: "$0.99"
Note the leading 0.

3)
249
30
Returns: "$249.30"

4)
1000
1
Returns: "$1,000.01"
"""


class FormatAmt:
    def amount(self, dollars, cents):
        dollars = [i for i in str(dollars)[::-1]]
        i = 3
        while i < len(dollars):
            dollars.insert(i, ",")
            i += 4
        if cents < 10:
            return "$" + "".join(dollars[::-1]) + ".0" + str(cents)
        else:
            return "$" + "".join(dollars[::-1]) + "." + str(cents)
