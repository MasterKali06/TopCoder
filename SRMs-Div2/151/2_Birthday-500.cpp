/*
Forgetting a close friend's birthday is quite embarrassing, but forgetting it two years in a row is a catastrophe. 
So what can a coder do to prevent this from happening again? Well, the thing he possibly can do best: code...
Given a String date (the current date) and a String[] birthdays, a list of people's birthdays and names, 
return a String, the date of the next occurring birthday, starting from the current date.
date is in the format "MM/DD" (quotes for clarity), where MM represents the two-digit month and DD represents 
the two-digit day (leading zero if necessary). Each element of birthdays is in the format "MM/DD <Name>" 
(quotes for clarity), where MM/DD is the date of <Name>'s birthday. <Name> is a sequence of characters from 
'A'-'Z' and 'a'-'z'. There is exactly one space character between the date and <Name>. The date returned also 
has to be in the format "MM/DD" (quotes for clarity).
 

Class:	Birthday
Method:	getNext
Parameters:	String, String[]
Returns:	String
Method signature:	String getNext(String date, String[] birthdays)    
 
Constraints
-	birthdays contains between 1 and 50 elements, inclusive.
-	Each element of birthdays contains between 7 and 50 characters, inclusive.
-	date and each element of birthdays follow the format described in the problem statement.
-	All dates are legal dates and neither date nor any date in birthdays is the 29th of February.
 
Examples
0)	
"06/17"
{"02/17 Wernie", "10/12 Stefan"}
Returns: "10/12"

1)	
"06/17"
{"10/12 Stefan"}
Returns: "10/12"

2)
"02/17"
{"02/17 Wernie", "10/12 Stefan"}
Returns: "02/17"

3)	
"12/24"
{"10/12 Stefan"}
Returns: "10/12"

4)
"01/02"
{"02/17 Wernie",
 "10/12 Stefan",
 "02/17 MichaelJordan",
 "10/12 LucianoPavarotti",
 "05/18 WilhelmSteinitz"}
Returns: "02/17"
*/

#include<iostream>
#include<vector>
#include<string.h>
#include<sstream>
#include<bits/stdc++.h>

using namespace std;

class Birthday{
	public:
		string getNext(string date, vector<string> birthdays){
			sort (birthdays.begin(), birthdays.end());
			for (int i=0; i<(int)birthdays.size(); i++){
				if (birthdays[i].substr(0, 5) >= date)
					return birthdays[i].substr(0, 5);
			}
			return birthdays[0].substr(0, 5);
		}
};