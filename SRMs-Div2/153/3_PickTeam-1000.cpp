/*
Problem Statement
A large company is trying to put together a team of people to work on some task. In order for any team to work well, 
the people involved must be able to get along with each other. The managers at the company have put together a list 
of potential candidates for the team, and have assigned a number to each pair of candidates, representing how well 
those two people get along. The more positive a number, the better two people get along, while the more negative a number, 
the more they dislike each other. The candidates are all well qualified, so at this point the only consideration is how well 
the team will get along. You are to pick which candidates to put on the team to maximize the sum of the numbers assigned 
to all of the pairs of people on the team. You will be given a String[], people, each of whose elements represents a single 
candidate, and an int, teamSize, representing the number of people to place on the team. Each element of people will be 
formatted as (quotes and angle brackets for clarity only):

"<name> <number0> <number1> <number2> ... <numberN>"
In other words, the element will start with the person's name, which will consist only of uppercase letters ('A'-'Z'), and 
will be followed by a single space delimited list of integers. The jth integer in the ith element will represent how well
person i gets along with person j and will be the same as the ith integer in the jth element. The ith integer in the ith 
element will always be 0 (how well a person gets along with himself). Your task is to return a String[], which contains 
the names of the people to put on the team (if more than one person on the team has the same name, that name must be in 
the returned String[] once for every member of the team with that name). The returned String[] should be sorted in ascending 
order. To make things simpler, there will only be one team which causes the maximum sum.

For example, if teamSize = 3 and people =

{"ALICE 0 1 -1 3",
 "BOB   1 0 2 -4",
 "CAROL -1 2 0 2",
 "DAVID 3 -4 2 0"}

There are four ways to create a team with 3 people. They give rise to the following sums:

ALICE, BOB, and CAROL: 1 + -1 + 2 = 2

ALICE, BOB, and DAVID: 1 + 3 + -4 = 0

ALICE, CAROL, and DAVID: -1 + 3 + 2 = 4

BOB, CAROL, and DAVID: 2 + -4 + 2 = 0

Of these, ALICE, CAROL and DAVID gives the highest sum, so your method would return {"ALICE","CAROL","DAVID"}.
 
    	
Class:	PickTeam
Method:	pickPeople
Parameters:	int, String[]
Returns:	String[]
Method signature:	String[] pickPeople(int teamSize, String[] people)    
 
Constraints
-	people will contain between 3 and 20 elements, inclusive.
-	Each element of people will contain between 7 and 50 characters, inclusive.
-	teamSize will be between 2 and the number of elements in people - 1, inclusive.
-	Each element of people will be formatted as a sequence of uppercase letters ('A'-'Z'), followed by a single 
	space delimited list of integers.
-	Each element of people will contain the same number of integers as there are elements in people.
-	Each integer in each element of people will be between -999 and 999, inclusive and will not have any extra leading zeros.
-	The ith integer of the jth element of people will be the same as the jth integer of the ith element of people.
-	The ith integer of the ith element will always be 0.
-	There will be only 1 way to make a team with the highest sum.
 
Examples
0)	
3
{"ALICE 0 1 -1 3",
 "BOB 1 0 2 -4",
 "CAROL -1 2 0 2",
 "DAVID 3 -4 2 0"}
Returns: { "ALICE",  "CAROL",  "DAVID" }
The example from above.

1)	    	
2
{"ALICE 0 1 -1 3",
 "BOB 1 0 2 -4",
 "CAROL -1 2 0 2",
 "DAVID 3 -4 2 0"}
Returns: { "ALICE",  "DAVID" }

2)	    	
2
{"A 0 -2 -2","B -2 0 -1","C -2 -1 0"}
Returns: { "B",  "C" }

3)	    	
13
{"A 0 2 8 7 1 -4 -3 1 8 2 8 2 1 -3 7 1 3 9 -6 -5",
 "A 2 0 0 7 -7 -5 8 -8 -9 -9 6 -9 -4 -8 8 1 7 0 3 3",
 "A 8 0 0 -5 -5 -7 1 -3 1 9 -6 6 1 5 6 -9 8 6 -8 -8",
 "A 7 7 -5 0 7 -5 3 9 8 3 -6 -5 -5 2 -6 2 -2 -1 -2 8",
 "B 1 -7 -5 7 0 7 -2 -9 3 7 0 -2 1 1 -9 -3 -2 2 1 -2",
 "B -4 -5 -7 -5 7 0 4 8 6 0 -1 4 1 -2 -9 4 0 -7 6 -2",
 "B -3 8 1 3 -2 4 0 8 -1 1 -2 -7 5 0 -6 9 0 -3 1 3",
 "B 1 -8 -3 9 -9 8 8 0 0 -2 5 0 5 8 3 5 2 4 5 4",
 "C 8 -9 1 8 3 6 -1 0 0 8 -3 8 -6 -4 7 -4 1 -5 5 4",
 "C 2 -9 9 3 7 0 1 -2 8 0 -9 -6 6 5 -8 -3 -8 2 2 4",
 "C 8 6 -6 -6 0 -1 -2 5 -3 -9 0 2 7 8 2 -6 -4 -6 4 4",
 "C 2 -9 6 -5 -2 4 -7 0 8 -6 2 0 0 -3 6 7 -1 2 -4 -2",
 "D 1 -4 1 -5 1 1 5 5 -6 6 7 0 0 -7 -4 8 -6 -3 4 -6",
 "D -3 -8 5 2 1 -2 0 8 -4 5 8 -3 -7 0 7 -3 5 -8 5 1",
 "D 7 8 6 -6 -9 -9 -6 3 7 -8 2 6 -4 7 0 9 -5 -5 -8 3",
 "D 1 1 -9 2 -3 4 9 5 -4 -3 -6 7 8 -3 9 0 -2 -7 8 -7",
 "E 3 7 8 -2 -2 0 0 2 1 -8 -4 -1 -6 5 -5 -2 0 6 0 5",
 "E 9 0 6 -1 2 -7 -3 4 -5 2 -6 2 -3 -8 -5 -7 6 0 4 8",
 "E -6 3 -8 -2 1 6 1 5 5 2 4 -4 4 5 -8 8 0 4 0 1",
 "E -5 3 -8 8 -2 -2 3 4 4 4 4 -2 -6 1 3 -7 5 8 1 0"}
Returns: { "A",  "A",  "B",  "B",  "B",  "B",  "C",  "C",  "C",  "D",  "D",  "D",  "E" }
*/


#include<bits/stdc++.h>
using namespace std;

const int MAX = 25;
int grid[MAX][MAX];

class PickTeam{
public:
	int sum = 0;			// saving the max sum
	vector<int> last = {};	// right combination according to the max sum

	// initializing a function that give unique possible combinaions of people in the teamsize range
	// using prev_permutation
	vector<int> comb(int n, int k){
		vector<int> comb = {};

		string bitmask(k, 1);
		bitmask.resize(n, 0);
		do {
			for (int i=0; i<n; i++)
				if (bitmask[i]) comb.push_back(i);

		} while (prev_permutation(bitmask.begin(), bitmask.end()));
		return comb;
	}

	// after the main comb we need to split every possible comb to pairs of 2 and return the sum
	int res(vector<int> cb, int t){
		int re = 0;
		vector<int> temp = comb(t, 2);
		int result[temp.size()];
		// we have a pattern (temp) from (cb = {0, 1, 2 ...}) and we make new ones according to it
		// example (cb = {0, 1, 2} -> temp = {0, 1, 0, 2, 1, 2}) ==> (new cb = {0, 1, 3}) -> result = {0, 1, 0, 3, 1, 3}
		for (int i=0; i<cb.size(); i++){
			for (int j=0; j<temp.size(); j++){
				if (temp[j] == i){
					result[j] = cb[i];
				}
			}
		}

		for (int i=0; i<temp.size(); i+=2){
			re += grid[result[i]][result[i+1]];
		}
		return re;
	}

	vector<string> pickPeople(int ts, vector<string> peop){
		
		vector<int> combs = comb(peop.size(), ts);
		vector<string> names(peop.size());
		// making a grid and a list of names from the input
		for (int i=0; i<peop.size(); i++){
			istringstream istr(peop[i]);
			istr >> names[i];
			for (int j=0; j<peop.size(); j++)
				istr >> grid[i][j];
		}

		if (peop.size() > 3){
			int i = 0,  j = 0;
			while (i < combs.size() / ts){
				vector<int> tmp = {};
				while(j<((i+1)*ts)){
					tmp.push_back(combs[j]);
					j++;
				}
				i++;
				// making a loop to give res each possible comb and find the max sum and by that best comb
				int conc = res(tmp, ts);
				if (conc > sum){
					sum = conc;
					last = tmp;
				}
			}
		}else{
			// this is for size of 3
			int cont = -9999;
			int f, l;
			for (int i = 0; i < peop.size(); i++){
				for (int j=0; j< peop.size(); j++)
					if (i!=j && grid[i][j]>cont){
						cont = grid[i][j];
						f = i;
						l = j;
					}
			}
			last.push_back(f);
			last.push_back(l);
		}

		// at last we discard the names according to our best combination and sort the names
		vector<string> result;
		for(int i=0; i<last.size(); i++)
			result.push_back(names[last[i]]);
		sort(result.begin(), result.end());
		return result;
	}
};

