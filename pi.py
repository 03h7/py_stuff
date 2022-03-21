# Pi digits search
from sys import *
from re import *
o=0
li=""
if(len(argv)<=1):exit("error: no inputs given")
if int(argv[1])<0 or int(argv[1])==-0:exit("Input must be positive")
p=open("pi1m.txt", "r").read()
i=p.find(argv[1])
if i==-1:exit("Input not found in the first million digits")
for a in finditer(argv[1], p):
    li=a.span()
    o+=1
print(f"Input {argv[1]} first found at index {i} and last found at index {li[0]}, {o} occurences")