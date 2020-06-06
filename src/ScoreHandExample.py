from time import time
from ScoreHand import ScoreHand

# if you have a deck of 52 cards, remove 4 cards (2 each for 2 players)
# leaves 48 in the deck. The number of possible 5 card communities that
# can be made from the 48 remaining cards will be 1,712,304. Multiply by
# number of players gives the number of times the hand evaluator would
# have to run to do a full brute force search of all possible communities
# to determine probability with 100% accuray.
num_loops = 1712304 * 2

hand = ['AC', '5H', '4H', '9C', 'TC', '2H', '3H']

start_time = time()

for i in range(num_loops):
	HandScore = ScoreHand(hand)

total_time = time() - start_time

print ("Hand:", hand)
print ("HandScore: %d" % HandScore)
print ("Total run time for %d evaluations: %.2f secs" % (num_loops, total_time))
print ("Evaluations per second: %d" % int(num_loops / float("%.2f" % total_time)))
