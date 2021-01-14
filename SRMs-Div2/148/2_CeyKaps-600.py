"""
Problem Statement
The keycaps on a keyboard have been switched around, and the user is now trying to remember what he was trying to type.
Create a class CeyKaps containing the method decipher that takes a String typed, representing the visible message on
the screen, and a String[] switched, representing the keycap switches. The method should return the original intended
message (what keys the user thought he was pressing).
A keycap can be switched around more than once. For example, if someone switched around 'A' and 'S', then switched
around 'S' and 'D', then 'D' would be where 'A' originally was, 'S' where 'D' was, and 'A' where 'S' was.
The elements of switches will be formatted as (quotes added for clarity) "*:*", where the *'s represent the keycaps to
be switched. The above example would be represented as: {"A:S","S:D","D:A"}, or alternately as {"S:A","D:S","A:D"} or
any other such combination. The order of the keycaps doesn't matter, but the order of the switches does.


Class: CeyKaps
Method: decipher
Parameters: string, tuple (string)
Returns: string
Method signature:
def decipher(self, typed, switches):

Notes
-	There is no restriction on how many times keycaps can be switched.
It is perfectly possible to return to the original keyboard configuration.

Constraints
-	typed will be between 1 and 50 characters in length, inclusive.
-	each character of typed will be an uppercase letter ('A'-'Z').
-	switches will contain between 1 and 50 elements, inclusive.
-	each element of switched will be formatted as (quotes added for clarity) "*:*" where each * represents a single
uppercase letter ('A'-'Z'), inclusive, but both *'s do not represent the same letter.

Examples
0)
"AAAAA"
{"A:B","B:C","A:D"}
Returns: "CCCCC"
At first, all keys look right. After the A:B switch, A looks like B and B looks like A. After the B:C switch,
A looks like C, B looks like A, and C looks like B. The third switch is irrelevant. Since "AAAAA" is what comes out,
Timmy must have been pressing "CCCCC".

1)
"ABCDE"
{"A:B","B:C","C:D","D:E","E:A"}
Returns: "AEBCD"

2)
"IHWSIOTCHEDMYKEYCAPSARWUND"
{"W:O","W:I"}
Returns: "WHOSWITCHEDMYKEYCAPSAROUND"
"""


class CeyKaps:
    def decipher(self, typed, switches):
        deciphered = ""
        for i in typed:
            for j in switches:
                if j[0] == i:
                    i = j[2]
                elif j[2] == i:
                    i = j[0]
            deciphered += i

        return deciphered
