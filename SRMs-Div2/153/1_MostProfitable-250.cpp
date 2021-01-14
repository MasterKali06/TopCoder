/*
When selling goods, it is important to know exactly how much it costs to acquire each item. A number of distributed 
costs, such as marketing often make this difficult, but not impossible. If a business can figure out how much an item 
costs, with some accuracy, then it can easily calculate the profit margins for the item. This information, combined 
with sales figures, can be used to determine which items are the most important to a business. In this problem you 
will be given the costs, prices, and number of sales for a number of items. Each element of costs represents the 
total costs accrued from selling a single item. The corresponding elements (ones with the same index) of prices and 
sales represent the prices at which single items are sold, and the number of sales of each item that have occurred 
in some time period, respectively. You are to return the name of the item (the corresponding element of items) that 
provides the business with the most profits. If there is a tie for the most profitable item, return the one that 
comes earliest in items (lowest index). If no item provides the business with positive profits you should return 
the empty String.
 
    	
Class:	MostProfitable
Method:	bestItem
Parameters:	int[], int[], int[], String[]
Returns:	String
Method signature:	String bestItem(int[] costs, int[] prices, int[] sales, String[] items)

Constraints
-	costs, prices, sales, and items will all contain the same number of elements.
-	costs, prices, sales, and items will contain between 1 and 50 elements, inclusive.
-	Each element of costs and prices will be between 1 and 1,000,000, inclusive.
-	Each element of sales will be between 0 and 1,000, inclusive.
-	Each element of items will have between 1 and 50 characters, inclusive.
-	Each character of each element of items will have ASCII value between 32 and 126, inclusive. 
	(All of the characters that can be easily made with a regular keyboard.)
 
Examples
0)	
{100,120,150,1000}
{110,110,200,2000}
{20,100,50,3}
{"Video Card","256M Mem","CPU/Mobo combo","Complete machine"}
Returns: "Complete machine"
This business makes 200 on video cards, loses 1000 on memory, makes 2500 on CPU/Mobo combos, and makes 3000 on 
complete machines. Since 3000 is the highest, you should return "Complete machine".

1)	
{100}
{100}
{134}
{"Service, at cost"}
Returns: ""
The only product given is sold at cost, so there are no items which give positive profit.

2)	
{38,24}
{37,23}
{1000,643}
{"Letter","Postcard"}
Returns: ""

3)	    	
{10,10}
{11,12}
{2,1}
{"A","B"}
Returns: "A"
*/


#include<bits/stdc++.h>
#include<iostream>
using namespace std;

class MostProfitable{
public:
	string bestItem(vector<int> costs, vector<int> prices, vector<int> sales, vector<string> items){

		int m = 0, index = -1, i = 0;
		while (i<costs.size()){

			if (costs[i] >= prices[i])
				i++;
			else{
				int temp = sales[i] * (prices[i] - costs[i]);
				if (temp>m){
					m = temp;
					index = i;
				}
				i++;
			}
		}
		if (index != -1)
			return items[index];
		else
			return "";
	}
};





























