# https://adventofcode.com/2020/day/10

"""
As this solution may not be obvious, here is the explanation:

If we sort our adapters (those from the example) in ascending order, we have a list:
(0)-1-4-5-6-7-10-11-12-15-16-19-(22)
where:
(0) - is the input Joltage
(22) - is the final (device's) Joltage
- [hyphen] - is elements' separator

We can replace each element with the number we have to add to it,
in order to get the next element (calculate difference list[n] - list[n+1]):
(1)-3-1-1-1-3-1-1-3-1-3-3-(X)
we don't need the last 2 values, since one of them is device's Joltage - we cannot change it,
and the second to last is always equal to 3, because:
"your device's built-in joltage ... 3 higher than the highest-rated adapter" 

Now we know:
1. We cannot change the elements (take out adapters) with 3, since it will create too big difference between elements
2. We cannot take out adapters after 3's, since it will also create too big "gap"
3. We cannot change the input Joltage = 0 -> first element with parentheses

So we can visualize the list like that:
(X)-X-A-A-X-X-A-X-X-X-X-X
where:
X - is the adapter we cannot take out,
A - is the adapter we can take out

For each A, there are two options:
it can be present in the sequence or not, so for this example there are 3 A,so the result is 2**3 = 8 

But for long chains of ones, there is a problem that we cannot take out 3 adjacent adapters:
(0)-1-2-3-4-5-6-(9)
cannot be changed into:
(0)-_-_-_-4-5-6-(9)

so, for each chain of 1s we generate all possible cases as binary strings,
where 1 means the adapter is present and 0 means the adapter is absent
and we count cases where there is no three or more adjacent zeros in such strings
So for:
(0)-1-2-3-4-5-6-(9)
it becomes:
(1)-1-1-1-1-1-3
so we have chain of ones of the length = 6, be we have to subtract 1 from each of such chains, since:
1. We cannot change the input Joltage - case for the first chain
2. One of ones is the one after 3. (Rule 2. from 'Now we know') - case for other chains

"""

import itertools as it
import re
import numpy as np

def countPossibilities(l):
    counter = 0
    possibilities = [''.join(seq) for seq in it.product("01", repeat=l)]
    for p in possibilities:
        if not re.search('000',p):
            counter += 1
    return counter


memoryMap = {}
adapters = []
with open('10data.txt','r') as f:
    for line in f:
        adapters.append(int(line))

adapters.sort()
diffs = list(np.array(adapters) - np.array([0] + adapters[:-1]))
diffsString = ''.join([ str(i) for i in diffs])
sequences = diffsString.split('3')
lenghts = [len(i) - 1 for i in sequences]

result = 1
for l in lenghts:
    if l > 0:
        try:
            result *= memoryMap[l]
        except KeyError:
            memoryMap[l] = countPossibilities(l)
            result *= memoryMap[l]
print(result)