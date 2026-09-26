from src.simulator import Simulator
import matplotlib.pyplot as plt
from src.viz import visualize
from src.input import start_simulating, take_input, update_progress, reset
import time
import sys


simulator = Simulator()


try:

    count = 10000
    while True:

        simulations = take_input(count)

        if not simulations:
            break

        start_simulating()

        decks = simulator.generate_decks(simulations)

        wins_by_trick, ties_by_trick, wins_by_card, ties_by_card = simulator.score(decks)

        count += decks.shape[0]

        # # Save decks here

        # # Update scores here

        # visualize(wins_by_trick, ties_by_trick, wins_by_card, ties_by_card, simulations)


        reset()


except KeyboardInterrupt:
    sys.exit(130)



