def score_int(hand, joker=False):
	if joker:
		bonus = hand.count('J')
		if bonus < 5:
			hand = hand.replace('J', '')
		else:
			bonus = 0
	counts = sorted((hand.count(s) for s in set(hand)))
	counts[-1] += bonus if joker else 0
	return sum(10 ** f for f in counts)

def score_frac(hand, joker=False):
	map = 'J23456789TQKA' if joker else '23456789TJQKA'
	return sum(map.index(s) / 10 ** (2 * i + 2) for i, s in enumerate(hand))

class Hand (object):
	def __init__(self, spec):
		hand, bid = spec.split()
		self.hand = hand
		self.bid = int(bid)
		self.score_1 = score_int(hand) + score_frac(hand)
		self.score_2 = score_int(hand, True) + score_frac(hand, True)

with open('input-07.txt') as file:
	hands = [Hand(line.strip()) for line in file]

hands.sort(key=lambda x: x.score_1)
print(f'Part 1: {sum((i + 1) * hand.bid for i, hand in enumerate(hands))}')
hands.sort(key=lambda x: x.score_2)
print(f'Part 2: {sum((i + 1) * hand.bid for i, hand in enumerate(hands))}')

