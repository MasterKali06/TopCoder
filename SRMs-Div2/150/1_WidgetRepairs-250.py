"""
Problem Statement
When a widget breaks, it is sent to the widget repair shop, which is capable of repairing at most numPerDay widgets per
day. Given a record of the number of widgets that arrive at the shop each morning, your task is to determine how many
days the shop must operate to repair all the widgets, not counting any days the shop spends entirely idle.
For example, suppose the shop is capable of repairing at most 8 widgets per day, and over a stretch of 5 days,
it receives 10, 0, 0, 4, and 20 widgets, respectively. The shop would operate on days 1 and 2, sit idle on day 3,
and operate again on days 4 through 7. In total, the shop would operate for 6 days to repair all the widgets.
Create a class WidgetRepairs containing a method days that takes a sequence of arrival counts arrivals (of type int[])
and an int numPerDay, and calculates the number of days of operation.


Class:	WidgetRepairs
Method:	days
Parameters:	int[], int
Returns:	int
Method signature:	int days(int[] arrivals, int numPerDay)


Constraints
-	arrivals contains between 1 and 20 elements, inclusive.
-	Each element of arrivals is between 0 and 100, inclusive.
-	numPerDay is between 1 and 50, inclusive.

Examples
0)
{ 10, 0, 0, 4, 20 }
8
Returns: 6
The example above.

1)
{ 0, 0, 0 }
10
Returns: 0

2)
{ 100, 100 }
10
Returns: 20

3)
{ 27, 0, 0, 0, 0, 9 }
9
Returns: 4

4)
{ 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6 }
3
Returns: 15
"""


class widgetRepairs:
    def days(self, arrivals, numPerDay):
        count = 0       # number of work days
        n = len(arrivals)
        i = 0
        remain = 0      # initialize remain to save the remaining widgets
        while i < n:
            # total save the remain and the arrived widgets
            total = remain + arrivals[i]
            if total == 0:      # if no widgets we pass
                i += 1
                continue
            else:               # else we increment the count
                count += 1
                remain = (arrivals[i] + remain) - numPerDay     # total - widgets repaired
                if remain < 0:
                    remain = 0
            i += 1
        # we need a condition for the widgets remained after the arrival finished
        if remain > 0:
            if remain % numPerDay != 0:
                count += (remain // numPerDay) + 1
            else:
                count += remain // numPerDay

        return count

