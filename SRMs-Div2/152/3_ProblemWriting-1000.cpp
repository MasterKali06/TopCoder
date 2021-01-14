/*
Problem Statement
Problem writers for TopCoder have to include constraints on their problems so that unexpected inputs don't get fed 
into unsuspecting code. Therefore, all problems written for TopCoder require a checkData function that takes the 
same parameters as the solution and prints an error message if the inputs violate the constraints. You're writing 
a nasty little problem about dot notation (used in one of your favorite logic textbooks written by Quine) and you 
need to write a checkData function to make sure that what's being passed into the problem is indeed in dot notation, 
and is within allowable string length, which is between 1 and 25 characters, inclusive. Dot notation is described in 
Backus-Naur form below; it tells you precisely how to construct all dot notations from their constituent parts
(double quotes are added for clarity, otherwise double quotes would be allowed in dot notation, and we don't want that.):

<DotNotation> := <Number> | <DotNotation><Dots><Operator><Dots><Number>
<Dots> := "" | <Dots>"."
<Operator> := exactly one of "+-/*"
<Number> := exactly one of "0123456789"
This reads as follows: Any single digit is a <DotNotation> because any digit by itself is a <Number>. 
Also, if you take any number of periods (<Dots>), a single <Operator> from line 3, any number of additional periods, 
and another single digit, you can concatenate that to any <DotNotation> and that new string would also be a <DotNotation>.
For example, "5" is a <DotNotation>, if you attach ".+.7" to it it becomes another <DotNotation>, and if you attach "*..3" to that 
("5.+.7*..3"), that also would be a <DotNotation>.
You will write a function called myCheckData (can't be called checkData, for this problem needs its own) that takes a 
String that may or may not be in dot notation, and returns a String about its validity. Check the input as follows below:
If the length of the String is illegal return the exact string "dotForm must contain between 1 and 25 characters, inclusive.".
Then check each character in the input from beginning to end; if the input is valid you'll return an empty String(don't return 
a null String!), which tells the Arena that the input is good.
Otherwise you'll want to tell the user what's wrong with the input; return the exact string "dotForm is not in dot notation, 
check character n.", replacing n with either the 0-indexed position of the first character that violates dot notation, or the 
length of the input if the dot notation is otherwise legal but incomplete.

    	
Class:	ProblemWriting
Method:	myCheckData
Parameters:	String
Returns:	String
Method signature:	String myCheckData(String dotForm)    
 
Constraints
-	dotForm will contain between 1 and 50 characters inclusive.
-	dotForm will consist solely of ASCII characters in the range 32-126 inclusive.
 
Examples
0)	    	
"3+5"
Returns: ""
Legal dot notation does not require dots in it.

1)	    	
"9..+.5...*....3"
Returns: ""
Again this dot notation is totally legal. Any number of dots are allowed around an operator.

2)	    	
"5.3+4"
Returns: "dotForm is not in dot notation, check character 2."
This is not legal dot notation as described in the Backus-Naur form. The first character to break from the form is character 2, because an operator was expected and a number was recieved.

3)    	
"9*9*9*9*9*9*9*9*9*9*9*9*9*9"
Returns: "dotForm must contain between 1 and 25 characters, inclusive."
Although this is legal dot notation, this is of illegal length.

4)	    	
"3.........../...........4"
Returns: ""
Just within the bounds of character length, and it's legal dot notation.
*/

#include<bits/stdc++.h>
#include<string>
#include<iostream>
using namespace std;

class ProblemWriting{
public:
	bool isnum(char c){
		return (c>='0') && (c<='9');
	}

	bool isop(char c){
		return (c=='*') || (c=='/') || (c=='+') || (c=='-');
	}


	string errat(int i){
		char ch[100];
		sprintf(ch, "dotForm is not in dot notation, check character %d.", i);
		return ch;
	}

	string myCheckData(string dotForm){
		if (dotForm.size()>25)
			return string("dotForm must contain between 1 and 25 characters, inclusive.");

		if (!isnum(dotForm[0]))
			return errat(0);

		bool num = true;
		for (int i=0; i<dotForm.size(); i++){
			
			char a = dotForm[i];
			if (isnum(a) && !num)
				return errat(i);

			if (isop(a) && num)
				errat(a);

			if (!isnum(a) && !isop(a) && a != '.')
				return errat(i);

			if (isnum(a)) num = false;
			if (isop(a)) num = true;
		}

		if (!isnum(dotForm[dotForm.size() - 1]))
			return errat(dotForm.size());
		
		return "";	
	}
};
