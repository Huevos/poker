HIGHCARD = 1
PAIR = 2
TWOPAIR = 3
TRIPS = 4
STRAIGHT = 5
FLUSH = 6
FULLHOUSE = 7
QUADS = 8
STRAIGHTFLUSH = 9

def GetHandCategory(score):
	# INPUT:
	# An integer between 1 and 7462, from score hand function

	# RETURN VALUE:
	# An integer between 1 and 9 representing the hand category.

	if score > 6185:
		return HIGHCARD;
	if score > 3325:
		return PAIR;
	if score > 2467:
		return TWOPAIR;
	if score > 1609:
		return TRIPS;
	if score > 1599:
		return STRAIGHT;
	if score > 322:
		return FLUSH;
	if score > 166:
		return FULLHOUSE;
	if score > 10:
		return QUADS;
	return STRAIGHTFLUSH;
