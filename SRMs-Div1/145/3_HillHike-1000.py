"""
Problem Statement
A hiker has set out to conquer a hill. The trail guide for the hill lists information known about the hill.
First, it lists how tall the hill is, and how far it is to the other side of the hill.Next, it gives a list of landmarks
that will be encountered while hiking the hill. The only things that are known about these landmarks are their height,
and the order in which they appear along the trail. Finally, on this hill, there are three types of terrain:

     _____
    /:   :\
   / :   : \
  /  :   :  \
 / 1 : 2 : 3 \

Type 1: rising terrain. In this type of terrain, the elevation of the hill rises one meter vertically for every meter
that is traveled horizontally.
Type 2: level terrain. In this type of terrain, the elevation of the hill remains constant.
Type 3:falling terrain.This terrain's elevation falls one meter vertically for every meter that is traveled horizontally
All three types of terrain can last for only multiples of one horizontal meter.
You will be given an int maxHeight (the maximum height of the hill, assuming the hill starts and ends at height 0),
an int distance (how far horizontally one must travel to hike over the top and reach the bottom on the other side),
and a int[] landmarks, which contains the heights of all the landmarks present on the trail.
The order of the elements in landmarks is the order in which they will be encountered on the trail.
All landmarks must be at least one horizontal meter apart.
Given all of this information, you must return how many different valid paths that the hiker could be facing.
A path on the hill is a sequence consisting only of the three types of terrain for the entire distance of the hill.
Two paths are different if and only if for at least one horizontal meter, the terrain type of one path is not the same
as the terrain type of another path. A path is valid if and only if the path:
1. Starts at height 0 and ends at height 0
2. Has no other locations with height 0, or height below 0 (otherwise it would be two hills, or a valley)
3. Has at least one point where the height is equal to maxHeight (otherwise, the hill would be smaller)
4. Does not go above maxHeight (otherwise, it would be taller)
5. Is laid out such that the landmarks could be placed in the order given at points on the trail. Note that two landmark
cannot appear at the same point on the trail, even if they are at the same height. they must be at least 1 meter apart
If no valid paths exist, return 0.


Class:	HillHike
Method:	numPaths
Parameters:	int, int, int[]
Returns:	long
Method signature:	long numPaths(int distance, int maxHeight, int[] landmarks)


Constraints
-	distance will be between 2 and 100, inclusive.
-	maxHeight will be between 1 and 50, inclusive.
-	landmarks will contain between 0 and 50 elements, inclusive.
-	Each element of landmarks will be between 1 and maxHeight, inclusive.
-	The return value will be less than or equal to 2^63 - 1 (it will fit into a long)

Examples
0)
5
2
{}
Returns: 3
There are three paths with a distance of 5 and a height of 2:

            _
           / \    _/\    /\_
          /   \  /   \  /   \
Distance: 12345  12345  12345

Notice that the 2nd and 3rd paths are mirror images, but are considered different. The following path cannot be used
because it does not have a height of 2, even though it has a length of 5.

 ___
/   \
12345

The following path has a height of 2 and a length of 5, but the beginning and ending points are not the only
points at height 0:

 /\
/  \_
12345

1)
2
45
{}
Returns: 0

2)
5
2
{2,2}
Returns: 1
The only path which could contain both landmarks is:

            _
           / \
          /   \
Distance: 12345

3)
8
3
{2,2,3,1}
Returns: 7

4)
38
11
{4,5,8,5,6}
Returns: 201667830444
"""

# couldnt solve this one yet .. im working on it .. todo
