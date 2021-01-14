"""
Problem Statement
The digits 3 and 9 share an interesting property. If you take any multiple of 3 and sum its digits, you get another
multiple of 3. For example, 118*3 = 354 and 3+5+4 = 12, which is a multiple of 3. Similarly, if you take any multiple
of 9 and sum its digits, you get another multiple of 9. For example, 75*9 = 675 and 6+7+5 = 18, which is a multiple of 9
Call any digit for which this property holds interesting, except for 0 and 1, for which the property holds trivially.
A digit that is interesting in one base is not necessarily interesting in another base. For example, 3 is interesting
in base 10 but uninteresting in base 5. Given an int base, your task is to return all the interesting digits for that
base in increasing order. To determine whether a particular digit is interesting or not, you need not consider all
multiples of the digit. You can be certain that, if the property holds for all multiples of the digit with fewer than
four digits, then it also holds for multiples with more digits. For example, in base 10, you would not need to consider
any multiples greater than 999.


Class:	InterestingDigits
Method:	digits
Parameters:	int
Returns:	int[]
Method signature:	int[] digits(int base)

Notes
-	When base is greater than 10, digits may have a numeric value greater than 9. Because integers are displayed in base
10 by default, do not be alarmed when such digits appear on your screen as more than one decimal digit. For example, one
of the interesting digits in base 16 is 15.

Constraints
-	base is between 3 and 30, inclusive.

Examples
0)
10
Returns: { 3,  9 }
All other candidate digits fail for base=10. For example, 2 and 5 both fail on 100, for which 1+0+0=1. Similarly,
4 and 8 both fail on 216, for which 2+1+6=9, and 6 and 7 both fail for 126, for which 1+2+6=9.

1)
3
Returns: { 2 }

2)
9
Returns: { 2,  4,  8 }

3)
26
Returns: { 5,  25 }

4)
30
Returns: { 29 }
"""


# logic: find the maxnum of the right base .. loop through multiples .. if sum of the multiple is not divisible remove
# it from the interesting list we made of all valid digits .. and we are done.
class InterenstingDigits:
    def digits(self, base):
        # finding the maxnum (3 digits) for the base
        n = 999     # maxnum for base 10
        mxnumBase = ""
        while n != 0:
            # find the last digit and concatenate to make a new number for the right base
            mxnumBase = str(n % base) + mxnumBase
            n //= base

        mxnumBase = int(mxnumBase)
        # here i add all the valid digits to a list
        interesting = [i for i in range(2, base)]

        nm = 0
        i = 2
        # outer loop
        for j in range(2, base):
            i = 2
            # loop through all the multiples of digits until the maxnum
            while i * j < mxnumBase:
                temp = i * j
                while temp != 0:
                    # finding the sum of the each multiple in the right base
                    nm += temp % base
                    temp //= base
                # if the sum is not divisible by the valid digit remove it from the interesting list and go to next
                if nm % j != 0:
                    interesting.remove(j)
                    nm = 0
                    break
                else:
                    # if the sum is divisible continue
                    # this way as the digit is already in the interesting list .. no action is needed till the loop ends
                    i += 1
                    nm = 0
                    continue

        return interesting
