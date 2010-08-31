def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    for line in open('gcd_testcases.dat'):
        values = line.split(', ')
        a = int(values[0])
        b = int(values[1])
        g = int(values[2])

        tc = gcd(a, b)
        if tc != g:
            print "Test failed for the case a=%d and b=%d. Expected %d. Obtained %d instead." % (a, b, g, tc)
            exit(1)

    print "All tests passed!"
