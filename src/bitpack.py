# import statements 
import numpy as np
import pandas as pd

# stores score totals from every simulation run
scores_file = 'data/processed/scores.csv'

def pack(decks: np.ndarray) -> np.ndarray:
    '''
    Pack each deck's card values (0, 1) as bytes.
    '''
    packed = np.packbits(decks, axis=1)
    return packed

def unpack(packed_decks: np.ndarray, size: int) -> np.ndarray:
    '''
    Unpack the packed decks to their original number of cards.
    '''
    decks = np.unpackbits(packed_decks, axis=1, count=size)
    return decks

def save(decks: np.ndarray, filename: str, seed: int) -> None:
    '''
    Pack and save one batch of deck simulations.
    '''
    packed_decks = pack(decks)
    np.savez(file=filename, packed_decks=packed_decks, seed=seed, simulations=decks.shape[0], size=decks.shape[1])

def load(filename: str) -> np.ndarray:
    '''
    Load and unpack decks from an .npz file.
    '''
    with np.load(filename, allow_pickle=False) as file:
        packed_decks = file['packed_decks']
        size = int(file['size'])

    decks = unpack(packed_decks, size)

    return decks

def combine(filenames: list[str]) -> np.ndarray:
    '''
    Load multiple saved deck files and combine them into one NumPy array.
    '''
    runs = []

    for filename in filenames:
        runs.append(load(filename))
    # stack every batch together by row
    combined_decks = np.concatenate(runs, axis=0)

    return combined_decks

def update_scores(wins_by_trick: np.ndarray, ties_by_trick: np.ndarray, wins_by_card: np.ndarray, ties_by_card: np.ndarray, simulations: int):
    '''
    Add results from the latest batch to the saved totals and rewrite the .csv file.
    '''
    try:
        old_scores = pd.read_csv(scores_file)
        # add saved to newest batch
        wins_by_trick += old_scores['wins_by_trick'].to_numpy().reshape(8, 8)
        ties_by_trick += old_scores['ties_by_trick'].to_numpy().reshape(8, 8)
        wins_by_card += old_scores['wins_by_card'].to_numpy().reshape(8, 8)
        ties_by_card += old_scores['ties_by_card'].to_numpy().reshape(8, 8)
    except FileNotFoundError:
        # only if there are no previous totals during the first run
        pass

    sequences = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']

    # one row for each of the 8x8 sequence combinations
    scores = pd.DataFrame({
        'my_choice': np.repeat(sequences, 8),
        'opponent_choice': np.tile(sequences, 8),
        'wins_by_trick': wins_by_trick.flatten(),
        'ties_by_trick': ties_by_trick.flatten(),
        'wins_by_card': wins_by_card.flatten(),
        'ties_by_card': ties_by_card.flatten(),
        'simulations': simulations
    })
    scores.to_csv(scores_file, index=False)

    return wins_by_trick, ties_by_trick, wins_by_card, ties_by_card

def save_combined(decks: np.ndarray, filename: str) -> None:
    '''
    Add the decks from the most recent batch to the saved combined deck file.
    '''
    try:
        old_decks = load(filename)
        combined_decks = np.concatenate([old_decks, decks], axis=0)
    except FileNotFoundError:
        combined_decks = decks

    # repack all decks and save
    packed_decks = pack(combined_decks)
    np.savez(file=filename, packed_decks=packed_decks, simulations=combined_decks.shape[0], size=combined_decks.shape[1])

def get_saved_count() -> int:
    '''
    Return the number of deck simulations recorded in the scores.csv file.
    '''
    try:
        scores = pd.read_csv(scores_file)
    except FileNotFoundError:
        # start at 0 if there aren't any saved simulations
        return 0
    return int(scores['simulations'].iloc[0])