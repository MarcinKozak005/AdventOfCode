# https://adventofcode.com/2020/day/12
import sys

with open('13data.txt','r') as f:
    earliestTimestamp = int(f.readline())
    busses = [ int(bus) for bus in f.readline().split(',') if bus!='x']

minimal = (0,sys.maxsize)
for bus in busses:
    mod = earliestTimestamp % bus
    timeToWait = bus-mod if mod!=0 else 0
    if timeToWait < minimal[1]:
        minimal = (bus, timeToWait)

# print(f'{minimal[0]} {minimal[1]}') 
print(minimal[0]*minimal[1])
    