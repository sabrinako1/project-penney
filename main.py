from src.simulator import Simulator
import matplotlib.pyplot as plt
from src.viz import visualize

simulations = 10_00

simulator = Simulator()

decks = simulator.generate_decks(simulations)

wins_by_trick, ties_by_trick, wins_by_card, ties_by_card = simulator.score(decks)

# Save decks here

# Update scores here

visualize(wins_by_trick, ties_by_trick, wins_by_card, ties_by_card, simulations)
