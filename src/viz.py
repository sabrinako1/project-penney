import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def visualize(p1_wins_by_trick, p1_ties_by_trick, p1_wins_by_card, p1_ties_by_card, num_decks):

    # SCORING BY CARDS
    plt.figure(figsize=(16, 8))
    cmap = sns.color_palette("Blues", as_cmap=True)
    cmap.set_bad("lightgray")
    cards_scores = (p1_wins_by_card/num_decks) * 100
    data = cards_scores
    np.fill_diagonal(cards_scores, np.nan)
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]
    plt.subplot(1, 2, 1)
    percent_wins_cards = (p1_wins_by_card/num_decks) * 100
    percent_ties_cards = (p1_ties_by_card/num_decks) * 100
    label_cards = np.array([[f"{win:.0f} ({tie:.0f})" for win, tie in zip(win_row, tie_row)]for win_row, tie_row in zip(percent_wins_cards, percent_ties_cards)])
    viz = sns.heatmap(data, annot=label_cards,fmt= "",cmap=cmap,xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad=12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    plt.title(f"My Probability of Win(Tie) Scoring By Cards \n N = {num_decks}")

    # SCORING BY TRICKS
    tricks_scores = (p1_wins_by_trick/num_decks) * 100
    data = tricks_scores
    np.fill_diagonal(tricks_scores, np.nan)
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]
    plt.subplot(1, 2, 2)
    percent_wins_tricks = (p1_wins_by_trick/num_decks) * 100
    percent_ties_tricks = (p1_ties_by_trick/num_decks) * 100
    label_tricks = np.array([[f"{win:.0f} ({tie:.0f})" for win, tie in zip(win_row, tie_row)]for win_row, tie_row in zip(percent_wins_tricks, percent_ties_tricks)])
    viz = sns.heatmap(data, annot=label_tricks,fmt="", cmap=cmap,xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad = 12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    plt.title(f"My Probability of Win(Tie) Scoring By Tricks \n N = {num_decks}")
    plt.tight_layout()
    plt.savefig("figures/heatmap.png", dpi=300, bbox_inches="tight")
