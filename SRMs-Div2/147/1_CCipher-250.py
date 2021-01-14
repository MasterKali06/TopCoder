"""
Problem Statement
Julius Caesar used a system of cryptography, now known as Caesar Cipher, which shifted each letter 2 places further
through the alphabet (e.g. 'A' shifts to 'C', 'R' shifts to 'T', etc.).
At the end of the alphabet we wrap around, that is 'Y' shifts to 'A'.
We can, of course, try shifting by any number. Given an encoded text and a number of places to shift, decode it.
For example, "TOPCODER" shifted by 2 places will be encoded as "VQREQFGT". In other words, if given (quotes for clarity)
"VQREQFGT" and 2 as input, you will return "TOPCODER". See example 0 below.


Class: CCipher
Method: decode
Parameters: string, integer
Returns: string
Method signature: def decode(self, cipherText, shift):

Constraints
-	cipherText has between 0 to 50 characters inclusive
-	each character of cipherText is an uppercase letter 'A'-'Z'
-	shift is between 0 and 25 inclusive

Examples
0)
"VQREQFGT"
2
Returns: "TOPCODER"

1)
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
10
Returns: "QRSTUVWXYZABCDEFGHIJKLMNOP"

2)
"TOPCODER"
0
Returns: "TOPCODER"

3)
"ZWBGLZ"
25
Returns: "AXCHMA"

4)
"DBNPCBQ"
1
Returns: "CAMOBAP"

5)
"LIPPSASVPH"
4
Returns: "HELLOWORLD"
"""

from string import ascii_uppercase


class CCipher:
    def decode(self, cipherText, shift):
        uppercase = ascii_uppercase
        decoded = ""
        for i in cipherText:
            decoded += uppercase[uppercase.find(i) - shift]

        return decoded
