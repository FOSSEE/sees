import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = random.sample(xrange(100), 10)
b = random.sample(xrange(1000), 10)
c = random.sample(xrange(10000), 10)
c = random.sample(xrange(10000), 10)
d = random.sample(xrange(100000), 10)
e = random.sample(xrange(1000000), 10)
f = a + b + c + d + e
f.sort()
a = random.sample(xrange(100), 10)
b = random.sample(xrange(1000), 10)
c = random.sample(xrange(10000), 10)
d = random.sample(xrange(100000), 10)
e = random.sample(xrange(1000000), 10)
g = a + b + c + d + e

testcases = []
for item in f:
    a = f[random.randrange(0, len(f))]
    b = g[random.randrange(0, len(g))]
    gc = gcd(a, b)
    testcases.append([a, b, gc])

sortedcases = sorted(testcases, key=lambda case: case[0])

fil = open('/home/madhu/Desktop/gcdtest.dat', 'w')
for case in sortedcases:
    fil.write('%d, %d, %d\n' % (case[0], case[1], case[2]))

fil.close()
