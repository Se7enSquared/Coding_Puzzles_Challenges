def distance(strand1, strand2):
	count = 0
	if len(strand1) != len(strand2):
	    raise ValueError
	else:
    	    for  i in range(0, len(strand1)):
    	    	if strand1[i] != strand2[i]:
    	    		count += 1
    	    return count

print(distance([1, 2, 3, 5], [1, 8, 4, 4))