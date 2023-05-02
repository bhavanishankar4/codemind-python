from math import sqrt
def solve(a):
   sq = int(sqrt(a))
   return (sq*sq) == a
a=int(input())
print (solve(a))