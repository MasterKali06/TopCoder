/*
You and your friends are setting up a fantasy TopCoder league, where you choose coders to be on your team and 
score points in the league when any one of your coders wins their room or successfully challenges somebody, etc. 
To be fair, a system has been developed to choose the order in which picks are distributed. It works like this: 
first, lots are drawn to choose your position in the league. Then the player with the first position gets first 
pick, the second player gets second pick, all the way until the last player picks. Then the order reverses: the 
last player chooses again, then the next to last player, and so on, until you reach the first player again. Then 
the cycle repeats: the first position chooses again, then the second, and so on.
For example: say you were in the third position on a 6 player league. You would get the 3rd pick, 
then you'd wait until the 10th pick (the order would be 1,2,you,4,5,6,6,5,4,you), and then the 15th pick, 
and so on until there were no more coders to choose. If there were 20 total picks, then you would get pick 
numbers 3,10,15.
Not wanting to miss your chance at a pick, your goal is to write a program that tells you what pick numbers you have 
in the order that you have them. You will receive three ints indicating your position in the league
(1 being the first position), the number of friends that are in the league with you, and the number of picks that 
are being divvied up among the league. You will return an int[] that indicates the picks that you receive in ascending order. 

    	
Class:	LeaguePicks
Method:	returnPicks
Parameters:	int, int, int
Returns:	int[]
Method signature:	int[] returnPicks(int position, int friends, int picks)    
 
Notes
Note that your position in the league and the pick numbers start at 1 and not 0. This should be clear from the examples.
 
Constraints
-	position will be between 1 and friends inclusive.
-	friends will be between 1 and 40 inclusive.
-	picks will be between 1 and 40 * friends inclusive.
 
Examples
0)    	
3
6
15
Returns: { 3,  10,  15 }
Example from above.

1)	    	
1
1
10
Returns: { 1,  2,  3,  4,  5,  6,  7,  8,  9,  10 }
You're the only player, so you get all the picks.

2)	    	
1
2
39
Returns: 
{ 1,  4,  5,  8,  9,  12,  13,  16,  17,  20,  21,  24,  25,  28,  29,  32,  33,  36,  37 }
You'll get the 1st and 4th picks in every set of 4.

3)	    	
5
11
100
Returns: { 5,  18,  27,  40,  49,  62,  71,  84,  93 }
You'll get the 5th and (2*11-5+1) or 18th picks out of every 2*11 picks.
*/

#include<bits/stdc++.h>
#include<vector>
#include<iostream>
using namespace std;

class LeaguePicks{
public:
	vector<int> returnPicks(int position, int friends, int picks){
		int limit = 0;
		int cons = friends;
		vector<int> mypick;

		while (limit<picks){
			for (int i = 1; i <= friends; i++){
				if (i<=picks && i == position){
					mypick.push_back(position);
					position = friends + (friends - position) + 1;
					friends += cons;
				}
				limit = i;
			}
			for (int i = friends+1; i<friends; i++){
				if (i<=picks && i == position){
					mypick.push_back(position);
					position = friends + (friends - position) + 1;
					friends += cons;
				}
				limit = i;
			}
		}
		return mypick;
	}
};


// an easier way
vector<int> returnPicks(int pos, int fr, int picks){
	vector<int> res;
	int i = 0;
	while (i<=picks){
		if (i+pos <= picks)
			res.push_back(i+pos);
		if (i+(fr*2)+1-pos<=picks)
			res.push_back(i+(fr*2)+1-pos);
		i += (fr*2);
	}
	return res;
}



