/*
Problem Statement
Inventory control is an important part of any business that maintains an inventory. On the one hand, businesses want to 
have enough of a product in stock that they can ship orders immediately. However, they do not want to have so much of a 
product in stock that all of their capital is tied up in that product. To deal with this, businesses often maintain a 
small stock, and replenish that stock as it is sold on a monthly basis. In other words, every month the business orders 
or produces more of a product so that it has some of the product in stock for the next month.
In this problem, a business wants to place a standing monthly order so that a certain number of items are delivered to 
it each month. Your task is to help the business determine how large a standing order to place. You will be given a int[], 
sales, representing the number of items that the business sold for each of a number of months, and are to determine how 
many they can expect to sell in an average month. Unfortunately, the business may have run out of items some months, 
so this is not as simple as just taking the average of the number of items sold each month.
You will be given a int[], daysAvailable, whose elements represent the number of days that the item was available in 
each of the months (elements of daysAvailable correspond to elements of sales with the same index). You should assume 
that, if the item was not available for a whole month, the business would have continued to sell the item at the same 
rate during the days of the month that it was not available as it did during the days the item was available, had sufficient 
stock been present. So, for example, if the business sold 5 items in the first half of a month, and then ran out, 
you can assume that they would have sold 10 items that month, if they had been available.
On months when the item was available for zero days, you can tell nothing about the number of items that might have sold, 
so you should not include these months in your calculation. Also, for simplicity, you may assume that all months have 30 days. 
Thus, if the item were in stock for exactly half of the month this would be represented by a 15 in daysAvailable. 
Furthermore, if the expected number of sales per month is not a whole number, you should round up since it is probably 
better to have one too many items than it is to have one too few.
 
    	
Class:	Inventory
Method:	monthlyOrder
Parameters:	int[], int[]
Returns:	int
Method signature:	int monthlyOrder(int[] sales, int[] daysAvailable)
    
Notes
-	While it is possible to solve this problem without using any double arithmetic, the last constraint ensures 
	that the simpler solution using doubles will work if an epsilon is used properly (pay special attention to the 
	last example). In other words, once you have computed the expected number of sales, you should subtract a small 
	number (like 1e-9) from this number before rounding up.
 
Constraints
-	daysAvailable and sales will have the same number of elements.
-	daysAvailable and sales will both have between 1 and 50 elements, inclusive.
-	Each element of daysAvailable will be between 0 and 30, inclusive.
-	Each element of sales will be between 0 and 10,000, inclusive.
-	If an element of daysAvailable is 0, the corresponding element of sales will also be 0.
-	At least one element of daysAvailable will be greater than 0.
-	The expected number of sales, prior to rounding, will not be within 1e-9 of an integer, unless the expected number 
	is exactly an integer.
 
Examples
0)	    	
{5}
{15}
Returns: 10
If 5 items are sold in 15 days (half a month), then 10 items could have been sold in a full month.

1)	
{75,120,0,93}
{24,30,0,30}
Returns: 103
The expected number of sales per month is 102.25. Rounding up, we get 103.

2)
{8773}
{16}
Returns: 16450

3)	    	
{1115,7264,3206,6868,7301}
{1,3,9,4,18}
Returns: 36091
Watch out for double imprecision. The expected number of sales per month, without rounding, is exactly 36091.
*/


#include<bits/stdc++.h>
using namespace std;

class Inventory{
public:
	int monthlyOrder(vector<int> s, vector<int> da){

		double temp = 0.0;
		int n = 0;
		for (int i=0; i<s.size(); i++){

			if (da[i] > 0){
				temp += (30.0*s[i]) / da[i];
				n++;
			}
		}
		temp = (temp - 0.000000001) / n;
		int ret = ceil(temp);
		return ret;
	}
};











