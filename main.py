from src.generator import Generator
import matplotlib.pyplot as plt

gen = Generator(simulations=10_000_000)

results = gen.run()

# B = 0, R = 1. First suit is 4x, second suit is 2x, third suit is 1x.
# BBB -> 0, BRB -> 2, BBR -> 1, RRR -> 7
combinations = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']

fig, ax = plt.subplots(figsize=(9, 7))
heatmap = ax.imshow(results)

ax.set_xticks(range(len(combinations)), labels=combinations)
ax.set_yticks(range(len(combinations)), labels=combinations)

plt.show()
