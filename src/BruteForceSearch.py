from NumHands import NumHands
from RunOneHand import RunOneHand

#	NOTES:
#
#	Function retains the keys from the input players array to use
#	as the keys of the returned dict so it is obvious which player
#	each result corresponds to (It doesn't matter what the keys are).
#
#	EXAMPLE "players" dict.
#	{
#		'P1': ['KH','QS'],
#		'P2': ['JD','QD']
#	}
#
#	"community" is a list of 0, 3 or 4 cards.
#
#	"dead" is a list of any cards that we know are no longer in play.

def BruteForceSearch(players, community = [], dead = [], DecimalPlaces = 2):
	CountCommunity = len(community)
	if CountCommunity not in (0,3,4):
		return False # not simulated play

	# get a full deck of cards
	deck = ['2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AC','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD','AD','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AS']

	# get a copy of the deck
	cards_left = list(deck)

	win = {}
	split = {}

	# remove anything we know is no longer in the deck
	for card in community + dead:
		cards_left.remove(card)
	for player in players:
		cards_left.remove(players[player][0])
		cards_left.remove(players[player][1])
		win[player] = 0
		split[player] = 0

	i0 = -1
	cnt = len(cards_left)

	if CountCommunity == 0: # pre-flop
		for i1 in range(i0+1, cnt-4):
			for i2 in range(i1+1, cnt-3):
				for i3 in range(i2+1, cnt-2):
					for i4 in range(i3+1, cnt-1):
						for i5 in range(i4+1, cnt-0):
							FakeCommunity = [cards_left[i1], cards_left[i2], cards_left[i3], cards_left[i4], cards_left[i5]]
							win, split = RunOneHand(players, FakeCommunity, win, split)

	elif CountCommunity == 3: # flop
		for i1 in range(i0+1, cnt-1):
			for i2 in range(i1+1, cnt-0):
				FakeCommunity = [cards_left[i1], cards_left[i2]] + community
				win, split = RunOneHand(players, FakeCommunity, win, split)

	elif CountCommunity == 4: # turn
		for i1 in range(i0+1, cnt-0):
			FakeCommunity = [cards_left[i1]] + community
			win, split = RunOneHand(players, FakeCommunity, win, split)

	# "div" is the number of hands we just tested
	div = NumHands(cnt, (5-len(community)))

	# Now create some output. The loop runs runs each player and creates a return dict for that player.
	rtn = {}
	for player in players:
		rtn[player] = {"win": "0.00", "split": "0.00"}
		rtn[player]["win"] = ("%." + str(DecimalPlaces) + "f") % ((100.0 * win[player])/div,)
		rtn[player]["split"] = ("%." + str(DecimalPlaces) + "f") % ((100.0 * split[player])/div,)
	return rtn
