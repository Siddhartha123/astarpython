from square import square

# quick test to see if the equality function between squares works properly
# this should be written up into a proper unit test
test_set = set()
sqone = square(0,0)
test_set.add(sqone)
sqtwo = square(0,0)
test_set.add(sqtwo)
print str(test_set)


