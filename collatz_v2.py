#Collatz conjecture between x and y, returns number with highest steps
from sys import *
i=1;a=argv;t=int;m=0;v=0
if(len(a)<=2):exit("error: no inputs given")
if t(a[1])<=0 or t(a[2])<=0:exit("error: negative number")
if t(a[1])>t(a[2]):exit("error: x greater than y")
def c(x):
 global i
 while x!=1:
  i+=1
  if x%2==0:x/=2
  else:x=x*3+1
 return i
for n in range(t(a[1]),t(a[2])+1):
 i=1;r=c(n)
 if m<r:m=r;v=n
print(f"{v}: {m} steps")