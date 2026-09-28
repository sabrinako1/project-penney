import numpy as np
import pandas as pd

scores_file = 'data/processed/scores.csv'

def pack(decks: np.ndarray) -> np.ndarray:
    packed = np.packbits(decks, axis=1)
    return packed

def unpack(packed_decks: np.ndarray, size: int) -> np.ndarray:
    decks = np.unpackbits(packed_decks, axis=1, count=size)
    return decks

def save(decks: np.ndarray, filename: str, seed: int) -> None:
    packed_decks = pack(decks)
    np.savez(file=filename, packed_decks=packed_decks, seed=seed, simulations=decks.shape[0], size=decks.shape[1])

def load(filename: str) -> np.ndarray:
    with np.load(filename, allow_pickle=False) as file:
        packed_decks = file['packed_decks']
        size = int(file['size'])

    decks = unpack(packed_decks, size)

    return decks

def combine(filenames: list[str]) -> np.ndarray:
    runs = []

    for filename in filenames:
        runs.append(load(filename))
    combined_decks = np.concatenate(runs, axis=0)

    return combined_decks

def update_scores(wins_by_trick: np.ndarray, ties_by_trick: np.ndarray, wins_by_card: np.ndarray, ties_by_card: np.ndarray, simulations: int):
    try:
        old_scores = pd.read_csv(scores_file)

        wins_by_trick += old_scores['wins_by_trick'].to_numpy().reshape(8, 8)
        ties_by_trick += old_scores['ties_by_trick'].to_numpy().reshape(8, 8)
        wins_by_card += old_scores['wins_by_card'].to_numpy().reshape(8, 8)
        ties_by_card += old_scores['ties_by_card'].to_numpy().reshape(8, 8)
    except FileNotFoundError:
        pass

    sequences = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']

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
    try:
        old_decks = load(filename)
        combined_decks = np.concatenate([old_decks, decks], axis=0)
    except FileNotFoundError:
        combined_decks = decks

    packed_decks = pack(combined_decks)
    np.savez(file=filename, packed_decks=packed_decks, simulations=combined_decks.shape[0], size=combined_decks.shape[1])

def get_saved_count() -> int:
    try:
        scores = pd.read_csv(scores_file)
    except FileNotFoundError:
        return 0
    return int(scores['simulations'].iloc[0])