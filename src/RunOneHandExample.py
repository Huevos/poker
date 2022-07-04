from RunOneHand import RunOneHand

players = {}

players['PlayerOne'] = ['KH','KD'] # keys can be any value
players['PlayerTwo'] = ['AC','5H']

FakeCommunity = ['4H', '9C', 'TC', '2H', '3H']

win = {}
split = {}

win, split = RunOneHand(players, FakeCommunity, win, split)

print("win", win)
print("split", split)

players['PlayerOne'] = ['KH','KD']
players['PlayerTwo'] = ['AH','5H']

win, split = RunOneHand(players, FakeCommunity, win, split)

print("win", win)
print("split", split)

players['PlayerOne'] = ['5C','6C']
players['PlayerTwo'] = ['5S','6S']

win, split = RunOneHand(players, FakeCommunity, win, split)

print("win", win)
print("split", split)

players['PlayerOne'] = ['AH','5H']
players['PlayerTwo'] = ['KH','KD']

win, split = RunOneHand(players, FakeCommunity, win, split)

print("win", win)
print("split", split)
