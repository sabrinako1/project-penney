import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def visualize(p1_wins_by_trick, p1_ties_by_trick, p1_wins_by_card, p1_ties_by_card, num_decks):

    plt.figure(figsize=(16, 8))

    # Selecting the color palette for the heatmap
    cmap = sns.color_palette("Blues", as_cmap=True)
    # Making the Nan values be a light grey color
    cmap.set_bad("lightgray")

    # SCORING BY CARDS
    cards_scores = (p1_wins_by_card/num_decks) * 100
    data = cards_scores

    # Setting the Nan values to be a light grey color
    np.fill_diagonal(cards_scores, np.nan)

    # For the x and y axis ticks
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]

    # Making the labels for each square be a percentage based on number of decks simulated
    percent_wins_cards = (p1_wins_by_card/num_decks) * 100
    percent_ties_cards = (p1_ties_by_card/num_decks) * 100
    # Creating labels for each square, wanting wins on outside, ties on inside of parenthesis
    label_cards = np.array([[f"{win:.0f} ({tie:.0f})" for win, tie in zip(win_row, tie_row)]for win_row, tie_row in zip(percent_wins_cards, percent_ties_cards)])

    # Creating the heatmap, wanted this heatmap to be to the left of the scoring by tricks heatmap
    plt.subplot(1, 2, 1)
    viz = sns.heatmap(data, annot=label_cards,fmt= "",cmap=cmap,xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)

    # Labeling the y and x axis by their corresponding player
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad=12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    # Title, as we want to show this data is from scoring by cards
    # Number of decks changes according to the simulations
    plt.title(f"My Probability of Win(Tie) Scoring By Cards \n N = {num_decks}")

    # SCORING BY TRICKS
    tricks_scores = (p1_wins_by_trick/num_decks) * 100
    data = tricks_scores

    # Setting the Nan values to be a light grey color
    np.fill_diagonal(tricks_scores, np.nan)

    # For the x and y axis ticks
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]

    # Making the labels for each square be a percentage based on number of decks simulated
    percent_wins_tricks = (p1_wins_by_trick/num_decks) * 100
    percent_ties_tricks = (p1_ties_by_trick/num_decks) * 100

     # Creating labels for each square, wanting wins on outside, ties on inside of parenthesis
    label_tricks = np.array([[f"{win:.0f} ({tie:.0f})" for win, tie in zip(win_row, tie_row)]for win_row, tie_row in zip(percent_wins_tricks, percent_ties_tricks)])

    # Creating the heatmap, wanted this one to be to the right of the scoring by cards heatmap 
    plt.subplot(1, 2, 2)
    viz = sns.heatmap(data, annot=label_tricks,fmt="", cmap=cmap,xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
   
    # Labeling the y and x axis by their corresponding player
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad = 12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)

    # Title, as we want to show this data is from scoring by cards
    # Number of decks changes according to the simulations
    plt.title(f"My Probability of Win(Tie) Scoring By Tricks \n N = {num_decks}")

    # Adjust spacing to ensure the two heatmaps don't have overlap
    plt.tight_layout()

    # Saving the heatmap as a PNG
    plt.savefig("figures/heatmap.png", dpi=300, bbox_inches="tight")
