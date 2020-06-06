from ScoreHand import ScoreHand

def RunOneHand(players, FakeCommunity, win, split):
	temp = {}
	for k in players.keys():
		SevenCardHand = FakeCommunity + players[k]
		temp[k] = ScoreHand(SevenCardHand)
	winningPlayers = [k for k,v in temp.items() if v == temp[min(temp, key=temp.get)]] # min(temp, key=temp.get) get the dict key (player name) of the winning player. But there could be multiple winners (split pot) so we need a list of all players with this score.
	if len(winningPlayers) == 1:
		if winningPlayers[0] not in win:
			win[winningPlayers[0]] = 0
		win[winningPlayers[0]] += 1
	else: # split pot
		for player in winningPlayers:
			if player not in split:
				split[player] = 0
			split[player] += 1
	return win, split