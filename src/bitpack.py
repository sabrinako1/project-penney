import numpy as np

def pack(decks: np.ndarray) -> np.ndarray:
    packed = np.packbits(
        decks,
        axis=1
    )
    return packed

def unpack(packed_decks: np.ndarray) -> np.ndarray:
    decks = np.unpackbits(
        packed_decks, 
        axis=1, 
        count=decks.shape[1]
    )
    return decks

def save(decks: np.ndarray, filename: str, seed: int) -> None:
    packed_decks = pack(decks)
    np.savez(
        file=filename, 
        packed_decks=packed_decks, 
        seed=seed,
        simulations=decks.shape[0],
        size=decks.shape[1]
    )

# if i ran 1k simulations and i wanna run another 50, unpack everything and then combine it together
# save each run as their own file
# (deck count, deck size)
# store decks every time i run i store a new deck, one file with the scores, t scores, and then update scores