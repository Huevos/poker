from math import factorial

def NumHands(n, r): # a.k.a. "n choose r"
	if n < r or r < 1:
		return 0
	# gets number of possible combinations
	return factorial(n) / factorial(r) / factorial(n-r)
