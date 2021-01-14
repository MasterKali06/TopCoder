"""
Problem Statement
Background
I remember a chain problem from my childhood. Suppose you have four sections of a golden chain. Each consists of three
links joined together in a line. You would like to connect all four sections into a necklace. The obvious solution is
to cut the last link of each section and use it to connect the first section to the second one, then the second to the
third, then the third to the fourth, then the fourth to the first one. If you want to minimize the number of cuts,
you can do better. You can cut one of the three link sections into its individual links. Using the three loose links
you can join the three remaining sections together.
Your task is, given the lengths of the sections, to return the minimum number of cuts to make one big circular necklace
out of all of them.

   
Class: GoldenChain
Method: minCuts
Parameters: tuple (integer)
Returns: integer
Method signature: def minCuts(self, sections):


Constraints
-	sections has between 1 and 50 elements inclusive
-	each element of sections is between 1 and 2,147,483,647 inclusive
-	the sum of all elements of sections is between 3 and 2,147,483,647 inclusive

Examples
0)
{3,3,3,3}
Returns: 3

1)
{2000000000}
Returns: 1

2)
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,
38,39,40,41,42,43,44,45,46,47,48,49,50}
Returns: 42

3)
{20000000,20000000,2000000000}
Returns: 3

4)
{10,10,10,10,10,1,1,1,1,1}
Returns: 5

5)
{1,10}
Returns: 1
"""


class GoldenChain:
    def minCuts(self, sections):

        sections = sorted(list(sections))
        link = 0
        for i in range(len(sections)):
            if link + sections[i] <= len(sections) - i - 1:
                link += sections[i]
            else:
                link += max(len(sections) - link - i, 0)

        return link
