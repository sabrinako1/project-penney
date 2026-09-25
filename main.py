from src.simulator import Simulator
import matplotlib.pyplot as plt
from src.viz import visualize

simulations = 10_000

simulator = Simulator()

decks = simulator.generate_decks(simulations)

p1_wins_by_trick, p1_ties_by_trick, p1_wins_by_card, p1_ties_by_card = simulator.score(decks)

visualize(p1_wins_by_trick, simulations)