import numpy as np

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
    pass