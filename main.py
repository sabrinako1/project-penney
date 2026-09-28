from src.simulator import Simulator
import matplotlib.pyplot as plt
from src.viz import visualize
from src.input import start_simulating, take_input, update_progress, reset
import time
import sys
from src.bitpack import save, save_combined
import os

os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

simulator = Simulator()

try:

    count = 0
    while True:
        
        
        simulations = take_input(count)

        if not simulations:
            break

        start_simulating()

        decks = simulator.generate_decks(simulations)

        wins_by_trick, ties_by_trick, wins_by_card, ties_by_card = simulator.score(decks)

        start = count + 1
        count += decks.shape[0]

        # # Save decks here
        filename = f'data/raw/{start}-{count}.npz'
        save(decks, filename, simulator.seed)
        save_combined(decks, 'data/raw/aggregated.npz')

        # # Update scores here

        # visualize(wins_by_trick, ties_by_trick, wins_by_card, ties_by_card, simulations)


        reset()


except KeyboardInterrupt:
    sys.exit(130)



