"""
A prefix code is a set of words in which no word is a prefix of another word in the set. A word v is said to be a prefix
of a word w if w starts with v.
An important property of prefix codes is that they are uniquely decodable. Prefix codes are commonly used - telephone
numbers are an everyday example (as you probably don't want a stranger to pick up the phone call you make just because
his number is a prefix of the number you intend to dial). Prefix codes are also very popular in computer science, the
Huffman code used for data compression being a famous example.
Given a String[] words, return the String "Yes" if that set of words is a prefix code or return the String "No, i" if
it is not, where i is replaced by the lowest 0-based index of a String in words that is a prefix of another String in
words. (That index should have no extra leading zeros.)


Class:	PrefixCode
Method:	isOne
Parameters:	String[]
Returns:	String
Method signature:	String isOne(String[] words)

Notes
-	Letters are case sensitive (e.g. "No" is not a prefix of "not").
-	Do not forget the single space between the comma and i in "No, i"

Constraints
-	words contains between 1 and 50 elements, inclusive.
-	Each element of words contains between 1 and 50 characters, inclusive.
-	Each element of words consists only of characters '0'-'9', 'A'-'Z' and 'a'-'z', inclusive.
-	No two elements of words are equal (as the input represents a set).

Examples
0)
{"trivial"}
Returns: "Yes"
As there is only one word, no word can be the prefix of another, so this is a trivial example of a prefix code.

1)
{"10001", "011", "100", "001", "10"}
Returns: "No, 2"
"100" (at index 2) and "10" (at index 4) are both a prefix of "10001" and "10" is also a prefix of "100", therefore it
is no prefix code. "100" is the prefix with the lowest index.

2)
{"no", "nosy", "neighbors", "needed"}
Returns: "No, 0"

3)
{"1010", "11", "100", "0", "1011"}
Returns: "Yes"

4)
{"No", "not"}
Returns: "Yes"
"""


class PrefixCode:
    def isOne(self, words):
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j][:len(words[i])]:
                    return "No, " + str(i)
                if words[j] in words[i][:len(words[j])]:
                    return "No, " + str(j)

        return "Yes"
