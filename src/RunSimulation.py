from RunOneHand import RunOneHand
import random

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
#	This function is for a pre-flop simulation. It is used speed is
#	needed rather than accuracy. A brute force search means we have
#	to test every possible combination, which means running several
#	million hands, whereas this function just runs the hole cards a
#	a few thousand times and comes up with a reasonably accurate
#	estimate of probability.
#
#	"dead" is a list of any cards that we know are no longer in play.

def RunSimulation(players, dead = [], div = 100000, DecimalPlaces = 2):
	# get a full deck of cards
	deck = ['2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AC','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD','AD','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AS']

	# get a copy of the deck
	cards_left = list(deck)

	win = {}
	split = {}

	# remove anything we know is no longer in the deck
	for card in dead:
		cards_left.remove(card)
	for player in players:
		cards_left.remove(players[player][0])
		cards_left.remove(players[player][1])
		win[player] = 0
		split[player] = 0

#	This block shuffles the cards and then plays them. Shuffling is quite time consuming so for each shuffle
#	the deck is cut up into blocks of 5 cards and each block is used rather than shuffling every time. This produces
#	the same results as shuffling before each hand but takes less time. The divider is the number of hands to
#	test. If we said 10,000 that would be 5,000 for each of 2 players or 3,333 for each of 3 players. Therefore
#	time for numerous players is similar to just 2 players but accuracy falls.

	div = int(div/len(players))
	steps = int(len(cards_left)/5)
	div2 = int(div/steps);
	for i1 in range(div2):
		random.shuffle(cards_left)
		for i2 in range(steps):
			FakeCommunity = cards_left[i2*5:i2*5+5]
			win, split = RunOneHand(players, FakeCommunity, win, split)

	# Now create some output. The loop runs runs each player and creates a return dict for that player.
	rtn = {}
	for player in players:
		rtn[player] = {"win": "0.00", "split": "0.00"}
		rtn[player]["win"] = ("%." + str(DecimalPlaces) + "f") % ((100.0 * win[player])/div,)
		rtn[player]["split"] = ("%." + str(DecimalPlaces) + "f") % ((100.0 * split[player])/div,)
	return rtn
