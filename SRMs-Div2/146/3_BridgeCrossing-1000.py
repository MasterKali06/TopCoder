"""
Problem Statement
A well-known riddle goes like this: Four people are crossing an old bridge. The bridge cannot hold more than two people
at once. It is dark, so they can't walk without a flashlight, and they only have one flashlight! Furthermore, the time
needed to cross the bridge varies among the people in the group. For instance, let's say that the people take 1, 2, 5
and 10 minutes to cross the bridge. When people walk together, they always walk at the speed of the slowest person.
It is impossible to toss the flashlight across the bridge, so one person always has to go back with the flashlight to
the others. What is the minimum amount of time needed to get all the people across the bridge?
In this instance, the answer is 17. Person number 1 and 2 cross the bridge together, spending 2 minutes.
Then person 1 goes back with the flashlight, spending an additional one minute. Then person 3 and 4 cross the bridge
together, spending 10 minutes. Person 2 goes back with the flashlight (2 min), and person 1 and 2 cross the bridge
together (2 min). This yields a total of 2+1+10+2+2 = 17 minutes spent.
You want to create a computer program to help you solve new instances of this problem. Given an int[] times,
where the elements represent the time each person spends on a crossing, your program should return the minimum possible
amount of time spent crossing the bridge.

   
Class: BridgeCrossing
Method: minTime
Parameters: tuple (integer)
Returns: integer
Method signature: def minTime(self, times):

Notes
-	In an optimal solution, exactly two people will be sent across the bridge with the flashlight each time
(if possible), and exactly one person will be sent back with the flashlight each time. In other words, in an optimal
solution, you will never send more than one person back from the far side at a time, and you will never send less than
two people across to the far side each time (when possible).

Constraints
-	times will have between 1 and 6 elements, inclusive.
-	Each element of times will be between 1 and 100, inclusive.

Examples
0)
{ 1, 2, 5, 10 }
Returns: 17
The example from the text.

1)
{ 1, 2, 3, 4, 5 }
Returns: 16
One solution is: 1 and 2 cross together (2min), 1 goes back (1min), 4 and 5 cross together (5min), 2 goes back (2min),
1 and 3 cross together (3min), 1 goes back (1min), 1 and 2 cross together (2min).
This yields a total of 2 + 1 + 5 + 2 + 3 + 1 + 2 = 16 minutes spent.

2)
{ 100 }
Returns: 100
Only one person crosses the bridge once.

3)
{ 1, 2, 3, 50, 99, 100 }
Returns: 162
"""


# definitly u can write this better .. but i think its the easiest way
# logic: first pair of fastest then pair of the slowest ... min of the other side always comes back ...
class BridgeCrossing:
    def minTime(self, times):
        times = list(times)
        temp = times
        past = 0

        slowest = sorted(times, reverse=True)
        fastest = sorted(times)
        if len(temp) <= 2:
            past += max(temp)

        if len(temp) == 3:
            past += sum(fastest[:2])
            temp.remove(max(fastest[:2]))
            past += max(temp)

        if len(temp) >= 4:
            past += sum(fastest[:2])
            temp.remove(slowest[0])
            temp.remove(slowest[1])
            past += max(slowest[:2])
            past += max(fastest[:2])
            if len(temp) == 2:
                past += max(fastest[:2])
            if len(temp) == 3:
                past += sum(fastest[:2])
                past += (max(fastest[1:3]))
            if len(temp) == 4:
                temp_slow = sorted(temp, reverse=True)
                temp_fast = sorted(temp)
                past += sum(temp_fast[:2])
                past += max(temp_slow[:2])
                past += max(temp_fast[:2])
                past += max(temp_fast[:2])

        return past

