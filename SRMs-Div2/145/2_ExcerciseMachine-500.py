"""
Problem Statement
You are writing firmware for an exercise machine.Each second, a routine in your firmware is called which decides whether
it should display the percentage of the workout completed.The display does not have any ability to show decimal points,
so the routine should only display a percentage if the second it is called results in a whole percentage of the total
workout.
Given a String time representing how long the workout lasts, in the format "hours:minutes:seconds", return the number of
times a percentage will be displayed by the routine. The machine should never display 0% or 100%.


    
Class: ExerciseMachine
Method: getPercentages
Parameters: string
Returns: integer
Method signature: def getPercentages(self, time):

Constraints
-	time will be a String formatted as "HH:MM:SS", HH = hours, MM = minutes, SS = seconds.
-	The hours portion of time will be an integer with exactly two digits, with a value between 00 and 23, inclusive.
-	The minutes portion of time will be an integer with exactly two digits, with a value between 00 and 59, inclusive.
-	The seconds portion of time will be an integer with exactly two digits, with a value between 00 and 59, inclusive
-	time will not be "00:00:00".

Examples
0)
"00:30:00"
Returns: 99
The standard 30 minute workout. Each one percent increment can be displayed every 18 seconds.

1)
"00:28:00"
Returns: 19
The 28 minute workout. The user completes 5 percent of the workout every 1 minute, 14 seconds.

2)
"23:59:59"
Returns: 0
This is the longest workout possible, given the constraints. No percentages are ever displayed on the screen.

3)
"00:14:10"
Returns: 49

4)
"00:19:16"
Returns: 3
"""


class ExerciseMachine:
    def getPercentages(self, time):
        time = [int(i) for i in list(time.split(":"))]
        seconds = time[0] * 3600 + time[1] * 60 + time[2]
        one_percent = float(seconds / 100)

        count = 0
        for i in range(1, 100):
            percent = one_percent * i
            if percent.is_integer():
                count += 1

        return count
