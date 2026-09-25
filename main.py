from src.generator import Generator
import matplotlib.pyplot as plt
from src.viz import visualize

simulations = 10_00

gen = Generator(simulations)

p1_wins_by_trick, p1_ties_by_trick, p1_wins_by_card, p1_ties_by_card  = gen.run()
visualize(p1_wins_by_trick, p1_ties_by_trick, p1_wins_by_card, p1_ties_by_card, simulations)