## https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

'''
Concepts: Arithmatic Progression, Sum of Series, Duplicate series reduction
For this problem we need to first identify the list of values which are natural numbers and less than given upper limit (say Ulimit)
Basic concept: The natural number divisible by 15 is also divisible by 3 and 5
We need to identify two series,
- Series A: {All natural numbers divisible by 3 and less than Ulimit}
- Series B: {All natural numbers divisible by 5 and less then Ulimit}
If we take intersection of Series A and Series B, we will get another Service C: {All natural numbers divisible by 15 and less than Ulimit}

If we add Series A and Series B, then Series C will be counted twice. So to achieve out result we need to do below calculation
          Result (R) =  Sum(All elements of Series A) + Sum (All elements of Series B) - Sum(All elemets of Series C) 

In case the upper limit is very high, by brute force, generating All these 3 series will be time counsuming as well as space consuming. To reduce time complexity 
and avoid any auxilary space, we will solve the problem by Arithmatic progression.

Arithmatic progression is like 1, 1+n, 1+2n, 1+3n, . . . , 1+mn, . . . 
Arithmatic progression for first N natural numbers is like AP(N)=> 1, 2, 3, 4, . . . , N
Sum of first N natual numbers = Sum of the elemnts present in arithmatic progression of first N natural numbers = (N(N+1))/2

For Series A, as all the elements are multiple of 3, so Series A is equal to an arithmatic progression=> 3, 3+(1x3), 3+(2x3), . . . , 3+(nx3)
if we simplify Series A, it will be like 
                 => 3, 3+(1x3), 3+(2x3), . . . , 3+(nx3)
                 => 3, 6, 9, . . . ., 3(n+1)
                 => 3x1, 3x2, 3x3, . . . , 3x(n+1)
If we re-write the series by dividing each of its elements by 3, then Series A will be look like 1, 2, 3, . . . ., n+1 => AP(N)
So Sum(All elements of Series A) = 3 x Sum(All elemnts of the AP(N)) => (3 x N x (N+1))/2
Similar way Sum (All elements of Series B) = (5 x N x (N+1))/2
and Sum(All elemets of Series C) => (15 x N x (N+1))/2

As in the question we are only aware of the upper count of the value limit and not the exact count of elements for each series, 
we will find the max multiplier for 3, 5 and 15 which will result max resulting value which is less than Ulimit for each case

Identify the max multiplier for 3:
    - if Ulimit is divisble by 3 then we will take temporary Ulimit as (Ulimit -1) because the input series is represnted as [1, Ulimit)
    - Divide the current Ulimit (or (Ulimit -1)) by 3 and take the floor value (lower box value)
    - Example: if Ulimit is 5 then 5/3 = 1.667 so the floor or lower box value will be 1

Wil identify max multiplier for 5 and 15 as well

Say we get multiplier as below
   - For 3 => three_mul
   - For 5 => five_mul
   - For 15 => fifteen_mul

These multipiers are the count of elemets for corresponding series as well namely Series A, B and C
Now if we transfor Result (R) =  Sum(All elements of Series A) + Sum (All elements of Series B) - Sum(All elemets of Series C)  with multiplier values, then

R = (3 x three_mul x (three_mul + 1))/2
    + (5 x five_mul x (five_mul + 1))/2
    - (15 x fifteen_mul x (fifteen_mul + 1))/2

We can further smplify the equation, by considering the difference between the Ulimit value and the max value of each series
    For Series A, max value will be 3 x three_mul
    So the difference between Ulimit and max value will be U3diff = (Ulimit - (3 x three_mul))
    Also we can re-write the relationship as (3 x three_mul) = Ulimit - U3diff
    So,
        3 x three_mul x (three_mul + 1) => (Ulimit - U3diff) X (three_mul + 1)

Let's re-write R in terms of Ulimit and UXdiff

R = ((Ulimit - U3diff) x (three_mul + 1))/2
    + ((Ulimit - U5diff) x (five_mul + 1))/2
    - ((Ulimit - U15diff) x (fifteen_mul + 1))/2
=> R = [((Ulimit - U3diff) x (three_mul + 1)) + ((Ulimit - U5diff) x (five_mul + 1)) - ((Ulimit - U15diff) x (fifteen_mul + 1))]/2
=> R = [(Ulimit x (three_mul + 1)) - (U3diff x (three_mul + 1)) + (Ulimit x (five_mul + 1)) - (U5diff x (five_mul + 1)) - (Ulimit x (fifteen_mul + 1)) + (U15diff x (fifteen_mul + 1))]/2
=> R = [Ulimit x (three_mul + 1 + five_mul + 1 - fifteen_mul - 1) - (U3diff x (three_mul + 1)) - (U5diff x (five_mul + 1))  (U15diff x (fifteen_mul + 1))]/2
=> R = [Ulimit x (three_mul + five_mul - fifteen_mul + 1) - (U3diff x (three_mul + 1)) - (U5diff x (five_mul + 1))  (U15diff x (fifteen_mul + 1))]/2

'''

if __name__ == '__main__':
    for _ in range(int(input())):
        upper_limit = int(input())
        
        three_mul = upper_limit // 3 if upper_limit % 3 != 0 else (upper_limit-1)//3
        three_diff_upper = upper_limit - (3 * three_mul)
        five_mul = upper_limit // 5 if upper_limit % 5 != 0 else (upper_limit-1)//5
        five_diff_upper = upper_limit - (5 * five_mul)
        fifteen_mul = upper_limit // 15 if upper_limit % 15 != 0 else (upper_limit-1)//15
        fifteen_diff_upper = upper_limit - (15 * fifteen_mul)
        
        result = (upper_limit * (three_mul + five_mul - fifteen_mul + 1) - (three_diff_upper * (three_mul + 1)) - (five_diff_upper * (five_mul + 1)) + (fifteen_diff_upper * (fifteen_mul + 1)))//2
        print(result)
