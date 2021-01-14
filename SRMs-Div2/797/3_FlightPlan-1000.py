"""
Problem Statement
There is a horizontal rectangular board with R rows and C columns of unit squares.
A three-dimensional world is built on top of this board: on each square of the board there is a stack of zero or more
unit cubes. The number of cubes on the square (r, c) is H[r*C + c].
We have a helicopter. The helicopter is negligibly tiny in comparison to the unit cubes that form the world, so we'll
pretend it's a point. The helicopter is currently standing in the middle of the top face of the stack of cubes on square (0, 0).
We want to get the helicopter to land in the opposite corner of the board: in the middle of the top face of the stack
of cubes at coordinates (R-1, C-1).
The helicopter can move in three ways: it can fly up, down, or sideways. Each time it moves, it must move by exactly
1 unit of distance. Flying an unit of distance upwards costs cup, flying the same distance downwards costs cdn, and
flying an unit of distance sideways costs clr. When flying sideways, the direction of travel must be one of the four
cardinal directions, so after each move the helicopter will be hovering over the center of one of the unit squares.
Obviously, the helicopter cannot leave the board and it cannot fly into a stack of cubes. It can fly while touching
the top surface of a stack of cubes, so for example the helicopter's first move can be sideways as long as it goes
into a square that doesn't have a higher stack of cubes.
Calculate and return the minimum total cost of reaching the helicopter's destination.
    
Class: FlightPlan
Method: fly
Parameters: integer, integer, tuple (integer), integer, integer, integer
Returns: long integer
Method signature: def fly(self, R, C, H, cup, cdn, clr):

Limits   
Time limit (s): 2.000
Memory limit (MB): 256
Stack limit (MB): 256

Constraints
- R will be between 1 and 50, inclusive.
- C will be between 1 and 50, inclusive.
- H will contain exactly R * C elements.
- Each element of H will be between 0 and 10^6, inclusive.
- cup, cdn and clr will each be between 1 and 10^6, inclusive.

Examples
0)  
1
5
{10, 8, 6, 8, 10}
40
10
20
Returns: 80
This world has just a single row. The helicopter both starts and wants to end in height 10, and as there are no obstacles
in its way, the cheapest solution is to simply fly horizontally (i.e., to the next column) four times.

1)  
6
1
{10, 8, 16, 18, 8, 12}
40
10
20
Returns: 480
One optimal solution looks as follows:
Start in row 0, column 0, with starting altitude 10.
Fly to the next row. (This costs 20 and results in a helicopter hovering 2 units of distance above the surface at this point.)
Fly 6 units upwards. (Cost 240, now the helicopter's altitude is 16.)
Fly to the next row. (Cost 20. We are now in the middle row and we are touching its surface.)
Fly another 2 units upwards. (Cost 80, now the helicopter's altitude is 18.)
Fly two units to the right. (Cost 40.)
Fly 6 units down. (Cost 60. We are now in row 0, column 4 and our altitude is 12.
Fly one unit to the right (cost 20), and as we have exactly the correct altitude, terminate.
The total cost is 480.

2)
5
5
{  100, 1000,  100,  100,  100,
    97, 9999, 9999, 9999,  100,
    93, 9999,    0, 9999,  100,
    99, 9999,   83,   65,  100,
    98,   93,   90, 9999,   95}
1000
1000
1
Returns: 5010
Flying up and down is very expensive. It's better to take a longer route, starting by moving from row 0 to row 1.

3)
5
5
{  100, 1000,  100,  100,  100,
    97, 9999, 9999, 9999,  100,
    93, 9999,    0, 9999,  100,
    99, 9999,   83,   65,  100,
    98,   93,   90, 9999,   95}
1
1
1000
Returns: 9805
The same map but now horizontal movement is expensive. Here it's better to travel through the square (0, 4).

4)    
1
1
{47}
123
234
345
Returns: 0
The obligatory example illustrating that travel starting and finishing at the same spot has cost 0.
"""
# sure there are better ways to do this
# didnt pass the system tests .. i know the corners but should work some new solution for this one later
from collections import deque


class FlightPlan:
    def fly(self, R, C, H, cup, cdn, clr):

        if R > 1 and C > 1:
            graph = []
            for i in range(0, len(H), C):
                graph.append(H[i:i + C])

            val0, val1, val2 = graph[0][0], graph[0][1], graph[1][0]
            alt1, alt2 = ((val1 - val0) * cup) + clr if val1 > val0 else clr, ((val2 - val0) * cup) + clr if val2 > val0 else clr

            final_res = []
            for i in {(1, 0), (0, 1)}:
                altitude = val0
                visited = {(0, 0), (0, 1), (1, 0)}
                queue = deque([i])
                if i == (1, 0):
                    if val2 > val0:
                        altitude = val2
                    horizontal = alt2

                if i == (0, 1):
                    if val1 > val0:
                        altitude = val1
                    horizontal = alt1

                while queue:
                    temp = []
                    vert = queue.popleft()
                    co = [(0, 1), (-1, 0), (1, 0), (0, -1)]
                    for i in range(len(co)):
                        dx = vert[0] + co[i][0]
                        dy = vert[1] + co[i][1]
                        if 0<=dx<=R-1 and 0<=dy<=C-1 and (dx, dy) not in visited:
                            temp.append((dx, dy))

                    val = []
                    for i in temp:
                        visited.add(i)
                        val.append(((graph[i[0]][i[1]] - altitude) * cup) + clr if graph[i[0]][i[1]] > altitude else clr)
                    if (R-1, C-1) in temp:
                        horizontal += clr
                        horizontal += abs(altitude - graph[R-1][C-1]) * cdn
                        final_res.append(horizontal)
                        break

                    if val:
                        index = val.index(min(val))
                        altitude = max(altitude, graph[temp[index][0]][temp[index][1]])
                        horizontal += min(val)
                        queue.append(temp[index])

            return min(final_res)

        else:
            horizontal = (max(C, R) - 1) * clr
            altitude = H[0]
            if max(H) > altitude:
                altitude = max(H)
                horizontal += (altitude - H[0]) * cup
                if altitude > H[-1]:
                    horizontal += (altitude - H[-1]) * cdn
            else:
                horizontal += (altitude - H[-1]) * cdn

            return horizontal

