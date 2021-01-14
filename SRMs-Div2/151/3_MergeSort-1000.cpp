/*
MergeSort is a classical sorting algorithm following the divide-and-conquer paradigm. 
Sorting n elements, it has a worst-case complexity of O(n*log(n)), which is optimal for sorting algorithms based on comparisons.
Basically, it sorts a list with more than one element the following way (a list containing only one element is always sorted):

    1. divide the list into two sublists of about equal size (divide)
    2. sort each of the two sublists (conquer)
    3. merge the two sorted sublists into one sorted list (combine)

A pro of MergeSort is that it is stable, i.e. elements with the same key value keep their relative order during sorting. 
A con is that it is not in-place since it needs additional space for temporarily storing elements.
Given a int[] numbers, return the number of comparisons the MergeSort algorithm (as described in pseudocode below) makes in order 
to sort that list. In this context, a single comparison takes two numbers x, y (from the list to be sorted) and determines 
which of x < y, x = y and x > y holds.

List mergeSort(List a)

    1. if size(a) <= 1, return a

    2. split a into two sublists b and c

       if size(a) = 2*k, b contains the first k elements of a, c the last k elements

       if size(a) = 2*k+1, b contains the first k elements of a, c the last k+1 elements

    3. List sb = mergeSort(b)

       List sc = mergeSort(c)

    4. return merge(sb, sc)

List merge(List b, List c)

    1. create an empty list a

    2. while both b and c are not empty, compare the first elements of b and c

       first(b) < first(c): remove the first element of b and append it to the end of a

       first(b) > first(c): remove the first element of c and append it to the end of a

       first(b) = first(c): remove the first elements of b and c and append them to the end of a

    3. if either b or c is not empty, append that non-empty list to the end of a

    4. return a

    	
Class:	MergeSort
Method:	howManyComparisons
Parameters:	int[]
Returns:	int
Method signature:	int howManyComparisons(int[] numbers)
 
Notes
-	Be sure to exactly follow the algorithm as described, as a different implementation of MergeSort might lead to a 
	different number of comparisons.
 
Constraints
-	numbers contains between 0 and 50 elements, inclusive.
-	Each element of numbers is an int in its 'natural' (signed 32-bit) range from -(2^31) to (2^31)-1.
 
Examples
0)    	
{1, 2, 3, 4}
Returns: 4
{1, 2, 3, 4} is first split to {1, 2} and {3, 4}. {1, 2} is split to {1} and {2} and merging to {1, 2} takes one comparison. 
{3, 4} is split to {3} and {4} and merging to {3, 4} also takes one comparison. Merging {1, 2} and {3, 4} to {1, 2, 3, 4} takes 
two comparisons (first 1 is compared to 3 and then 2 is compared to 3). This makes a total of four comparisons.

1)	
{2, 3, 2}
Returns: 2
{2, 3, 2} is split to {2} and {3, 2}. {3, 2} is split and then merged to {2, 3} making one comparison. {2} and {2, 3} 
are merged to {2, 2, 3} also making one comparison, which totals to two comparisons made.

2)    	
{-17}
Returns: 0

3)
{}
Returns: 0

4)
{-2000000000,2000000000,0,0,0,-2000000000,2000000000,0,0,0}
Returns: 19
*/

#include<bits/stdc++.h>

using namespace std;

class MergeSort{
public:
	
	int count;

	vector<int> divider(vector<int> slices){
		vector<int> b, c;
		if (slices.size() <= 1) return slices;
		for (int i=0; i<slices.size()/2; i++) b.push_back(slices[i]);
		for (int i=slices.size()/2; i<slices.size(); i++) c.push_back(slices[i]);
		vector<int> sb = divider(b), sc = divider(c);
		return merge(sb, sc);
	}

	vector<int> merge(vector<int> b, vector<int> c){
		vector<int> slices;
		int ib=0, ic=0;

		while (ib < b.size() && ic < c.size()){
			int fb = b[ib], fc = c[ic];
			count ++;
			if (fb < fc){
				slices.push_back(fb);
				ib++;
			}else if(fb > fc){
				slices.push_back(fc);
				ic++;
			}else{
				slices.push_back(fb);
				slices.push_back(fc);
				ib++, ic++;
			}
		}

		while (ib < b.size()){
			slices.push_back(b[ib++]);
		}
		while (ic < c.size()){
			slices.push_back(c[ic++]);
		}
		return slices;
	}


	int howManyComparisons(vector<int> numbers){
		 count = 0;
		 divider(numbers);
		 return count;
	}
};






















