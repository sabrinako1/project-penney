## ABOUT PENNEY'S GAME
Penney's Game is a game in which two players pick a combination of 3 coin flips (composed of either Heads or Tails).  

For example, Player A could select Heads, Heads, Tails. Player B could select Tails, Heads, Tails.

Then, a coin is continuously flipped. A player wins the game when their combination is consecutively met by flipping the coin. Continuing the example above, if the coin is flipping and has just been Tails, then Heads, then Tails, Player B wins as their combination has been met before Player A. 

## ABOUT HUMBLE-NISHIYAMA (H-N) RANDOMNESS GAME
### Scoring by Tricks:
The H-N game is a version of Penney's Game, played with a deck of cards rather than a coin. There are two ways to score the H-N game, by Tricks and by Cards, we'll begin by describing how to score by tricks.

In this game, two players pick a combination of 3 cards (composed of either Red or Black). 

For example, player A could selected Red, Red, Black. Player B could selected Black, Red, Black. 

Then, cards of the deck are flipped. The players watch the cards to see if either combination has been fulfilled consecutively. Continuining the example above, if the cards flipped are Red, then Red, then Black, then player A wins that "trick", and those cards and all of the cards it took to get there are set aside. Therefore, if it took 5 cards to get to fulfill a combination, a player receives one "trick", not 5 cards.

The game continues until there is another combination fulfilled (and then all the cards it took to fulfill that combination are set aside and deemed another "trick"). This goes on until there are no more cards in the deck left to fulfill a combination.

At the end of the game, both players count up how many "tricks" they won. The player with the higher amount of "tricks" wins the game. If both players were had the same amount of tricks, they tie.

### Scoring by Cards: 
Another way to score is by cards. In this scoring version, the game stays the same, however each time a player's combination is met, the player wins the number of cards it took to reach the combination. Therefore, if it took 5 cards to get to fulfill a combination, a player is awarded the 5 cards, not one "trick". 

Those cards are set aside, and the game continues until the next combination is met. When the next combination is met, the number of cards it took to get there, are awarded to whichever player's combination it was. 

At the end of the game, both players count up how many cards they were awarded. The player with the higher amount of cards wins the game. If both players end the game with the same amount of cards, they tie. 

## PURPOSE OF THE INVESTIGATION
The purpose of the investigation is to analyze the differences in each of the card combinations in the H-N game, and looking at the differences in these combinations when scored by tricks vs cards. 

Ultimately, when looking at these differences, we can aim to find the best strategy possible when scored by tricks or cards.

## HOW TO RUN
This project uses the Python package manager uv, so if not installed go to https://docs.astral.sh/uv/ to install based on your operating system. After you've installed, run the program with:
```python
uv run main.py
```
What will be displayed a large PENNEY 67 card design above the number of decks that have already been simulated. If this is your first run, it should be 0 but if you should happen to run it multiple times, the number of deck simulations is saved and will continue to accumulate! Below that is where you can enter an additional amount of decks to simulate. New decks are generated, scored, and then updated with the previously run decks. The raw decks, processed results, and updated heatmaps are then saved in their respective directories (data for the decks/results and figures for the heatmaps).

## OUR FINDINGS
Our final results are based on 6767676 randomly simulated decks, where each one was used to evaluate the 56 valid combinations of three-card sequences. By looking at the heatmap, we can determine the best response to each opponent choice by selecting the highest win percentage in each row. 
### Opponent Choice --> Best Response by Cards | Best Response by Tricks
1. BBB --> RBB | RBB
2. BBR --> RBB | RBB
3. BRB --> RRB | BBR
4. BRR --> BBR | BBR
5. RBB --> RRB | RRB
6. RBR --> BBR | RRB
7. RRB --> BRR | BRR
8. RRR --> BRR | BRR

This shows that the player who chooses their sequence second has the advantage since they are able to respond their opponent's initial choice. BRB and RBR are the safest first picks because they give the opponent's counter the smallest advantage. The best responses win around 89-100% of rounds by cards and 79-99% by tricks. These results are pretty consistent between by card and by trick, as 6 of the 8 sequences for the opponent's choice have the same optimal response. They were also basically the same between 100067 and 6767676 decks, showing that the results level out after a sufficiently large number of simulations.