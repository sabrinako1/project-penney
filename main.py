from src.generator import Generator
import matplotlib.pyplot as plt
from src.viz import visualize

simulations = 10_000

gen = Generator(simulations)

p1_wins = gen.run()
visualize(p1_wins,simulations)