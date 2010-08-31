def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    tc1 = gcd(48, 64)
    if tc1 != 16:
        print "Test failed for the case a=48 and b=64. Expected 16. Obtained %d instead." % tc1
        exit(1)

    tc2 = gcd(44, 19)
    if tc2 != 1:
        print "Test failed for the case a=44 and b=19. Expected 1. Obtained %d instead." % tc2
        exit(1)

    print "All tests passed!"
