import random
import numpy as np

class Generator:
	def __init__(self, simulations: int = 10000, seed: int = 1):
		self.simulations = simulations
		self.rng = np.random.default_rng(seed=seed)
		self.deck = np.array([0] * 26 + [1] * 26)

	def run(self):
		# One deck per simulation
		decks = np.tile(self.deck, (self.simulations, 1))

		# Shuffle decks
		decks = self.rng.permuted(decks, axis=1)

		# Get the three card pattern at each index
		deck_patterns = 4*decks[:, :-2] + 2*decks[:, 1:-1] + decks[:, 2:]

		p1 = self.rng.integers(0, 8, size=self.simulations)
		p2 = self.rng.integers(0, 7, size=self.simulations)
		p2 += p2 >= p1

		choices = np.arange(8)

		current_positions = np.full((self.simulations, 8, 8), 0)
		still_running = np.full((self.simulations, 8, 8), True)

		# simulations x 8 x 52
		matches = deck_patterns[:, None, :] == choices[None, :, None]

		# simulations x 8 x 8
		first, second = np.broadcast_arrays(
				matches[:, :, None, :],  # simulations x 8 x 1 x 50
				matches[:, None, :, :]   # simulations x 1 x 8 x 50
			)

		# simulations x 8 x 8 x 50 x 2
		pairs = np.stack((first, second), axis=-1)
		indices = np.arange(50)[None, None, None, :]

		p1_wins = np.full((8, 8), 0)

		while still_running.any():
			mask = indices >= current_positions[:, :, :, None]

			masked_pairs = np.where(mask[..., None], pairs, False)
			player_plays = np.argmax(masked_pairs, axis=-2)
			player_plays[player_plays == 0] = 50
			diffs = player_plays[:,:,:,0] - player_plays[:,:,:,1]
			plays = np.min(player_plays, axis=3)

			play_diffs = plays - current_positions
			p1_wins += (diffs > 0).sum(axis=0)

			current_positions = plays + 3

			still_running = (current_positions < 50).any()

		# current_positions = 

		# 	p1_wins = plays_until_win[:, :, None] < plays_until_win[:, None, :]
		# 	current_positions = np.minimum(plays_until_win[:, :, None], plays_until_win[:, None, :])
			

		# # Get minimum index of first match, 50 otherwise

		# # p1_wins = (plays_until_win[:, :, None] < plays_until_win[:, None, :]).sum(axis=0)
		# # print(p1_wins)

		# return p1_wins.sum(axis=0)

		# first_p1 = np.where(p1[:, None] == deck_patterns, indices, 50).min(axis=1)
		# first_p2 = np.where(p2[:, None] == deck_patterns, indices, 50).min(axis=1)

		# p1_wins = first_p1 < first_p2

		# # Get counts of every unique combination, with p2 choice as row and p1 choice as column.
		# grid = np.bincount(p1[p1_wins] + 8 * p2[p1_wins], minlength=64).reshape(8, 8)

		return p1_wins

		

# class Generator:
# 	def __init__(self, simulations: int = 10000, seed: int = 1):
# 		self.simulations = simulations
# 		self.rng = random.Random(seed)
# 		self.deck = ['B'] * 26
# 		self.deck.extend(['R'] * 26)

# 	def run(self):
# 		options = []

# 		for one in ['B', 'R']:
# 			for two in ['B', 'R']:
# 				options.extend(''.join(one + two + three) for three in ['B', 'R'])

# 		results = {p1: dict.fromkeys(options, 0) for p1 in options}

# 		for i in range(self.simulations):
# 			p1_choice, p2_choice, winner = self._play_round()

# 			if winner == 'p1':
# 				results[p1_choice][p2_choice] += 1

# 		return results


# 	def _play_round(self):
# 		p1 = self._get_choice()
# 		p2 = self._get_choice(p1)

# 		self.rng.shuffle(self.deck)

# 		for i in range(len(self.deck) - 2):
# 			option = ''.join(self.deck[i:i+3])
# 			if option == p1:
# 				return p1, p2, 'p1'
# 			elif option == p2:
# 				return p1, p2, 'p2'

# 		return p1, p2, None


# 	def _get_choice(self, previous_choice: str | None = None) -> str:
# 		choice = None
# 		while choice is None or choice == previous_choice:
# 			choice = ''.join(self.rng.choice(['R', 'B']) for _ in range(3))

# 		return choice