"""
Problem Statement    
Computers tend to store dates and times as single numbers which represent the number of seconds or milliseconds since a
particular date. Your task in this problem is to write a method whatTime, which takes an integer, seconds, representing
the number of seconds since midnight on some day, and returns a string formatted as "<H>:<M>:<S>". Here, <H>
represents the number of complete hours since midnight, <M> represents the number of complete minutes since the last
complete hour ended, and <S> represents the number of seconds since the last complete minute ended. Each of <H>, <M>,
and <S> should be an integer, with no extra leading 0's. Thus, if seconds is 0, you should return "0:0:0", while if
seconds is 3661, you should return "1:1:1".
Definition
    
Class: Time
Method: whatTime
Parameters: integer
Returns: string
Method signature: def whatTime(self, seconds):

Limits
Time limit (s): 2.000
Memory limit (MB): 64
Constraints
-
seconds will be between 0 and 24*60*60 - 1 = 86399, inclusive.
Examples
0)   
0
Returns: "0:0:0"

1)   
3661
Returns: "1:1:1"

2)
 
5436
Returns: "1:30:36"

3)
 
86399
Returns: "23:59:59"
"""


class Time:
    def WhatTime(self, seconds):
        time_list = [0, 0, 0]
        time_list[0] = seconds // 3600
        time_list[1] = (seconds % 3600) // 60
        time_list[2] = (seconds % 3600) % 60
        time_list = [str(i) for i in time_list]
        return ":".join(time_list)
