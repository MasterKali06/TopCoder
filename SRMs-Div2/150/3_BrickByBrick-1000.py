"""
Problem Statement
You are given a rectangular map in which each space is marked with one of three characters: '.' (open), 'B' (a brick),
or '#' (an indestructible block). Walls made of indestructible blocks surround the field on all sides, but are not shown
on the map. A ball is bouncing around this map, destroying bricks, and your task is determine how long it takes the ball
to destroy all the bricks.
The top left space of the map is always open, and this is where the ball begins. More specifically, the ball begins at
time 0 in the middle of the top edge of this space (see the diagram in Example 0). The ball is traveling diagonally down
and to the right at a speed of half a meter per second vertically, and half a meter per second horizontally. Each space
is 1 meter square, so the ball crosses half a space vertically and half a space horizontally each second.
Whenever the ball strikes the edge of an obstacle--either a brick or an indestructible block--it bounces off at an angle
perpendicular to its incoming path. The ball will never hit two obstacles simultaneously. Whenever the ball bounces off
a brick, the brick is destroyed and removed from the map.
Your method should return the time at which the last brick is destroyed. If one or more bricks will never be destroyed,
return -1.


Class:	BrickByBrick
Method:	timeToClear
Parameters:	String[]
Returns:	int
Method signature:	int timeToClear(String[] map)


Constraints
-	map contains between 1 and 15 elements, inclusive.
-	All elements of map contain the same number of characters (between 1 and 15, inclusive).
-	All elements of map contain only the characters '.', 'B', and '#'.
-	The top left corner of map (that is, the first character of the first element) is '.'.
-	map contains at least one 'B'.

Examples
0)
{ ".B",
  "BB" }
Returns: 6

The following diagram illustrates the path of the ball.

     __0________
    | / \ |     |
    |/   \|     |
    3  .  1  B  |
    |\   /|\    |
    | \ / | \   |
    |--2--|--6--|
    |     |     |
    |     |     |
    |  B  |  B  |
    |     |     |
    |_____|_____|

The ball begins at point 0, traveling down and to the right. It bounces off the first brick at time 1, and off the
second brick at time 2. At time 3, it bounces off the left wall, and at time 4 it bounces off the upper wall at the
same place it started. At time 6, the ball destroys the third and final brick, so the method returns 6.

1)
{ ".BB",
  "BBB",
  "BBB" }

Returns: -1
The ball will never hit the brick in the bottom right corner.

2)
{ "......B",
  "###.###",
  "B.....B" }

Returns: 35

3)
{ "..BBB...",
  ".#BB..#.",
  "B.#B.B..",
  "B.B.....",
  "##.B.B#.",
  "#BB.#.B.",
  "B..B.BB.",
  "#..BB..B",
  ".B....#." }

Returns: -1

4)
{ ".BB..BBB.B...",
  "B.B...B..BB..",
  "#B...B#B.....",
  "B#B.B##...##B",
  "BB.B#.B##B.B#",
  "B.B#.BBB.BB#B",
  "B#BBB##.#B#B.",
  "B#BB.BBB#BB.#" }

Returns: 3912

5)
{ ".BBBBBBBBBBBBBB",
  "##############B",
  "BBBBBBBBBBBBBBB",
  "B##############",
  "BBBBBBBBBBBBBBB",
  "##############B",
  "BBBBBBBBBBBBBBB",
  "B##############",
  "BBBBBBBBBBBBBBB",
  "##############B",
  "BBBBBBBBBBBBBBB",
  "B##############",
  "BBBBBBBBBBBBBBB",
  "##############B",
  "BBBBBBBBBBBBBBB" }

Returns: 31753
"""