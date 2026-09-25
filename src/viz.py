import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def visualize(p1_wins_by_trick, p1_ties_by_trick, p1_wins_by_card, p1_ties_by_card, num_decks):

# SCORING BY CARDS
    cards_scores = (p1_wins_by_card/num_decks) * 100
    data = cards_scores
    cards_scores[cards_scores == 0] = -1
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]
    plt.subplot(1, 2, 1)
    viz = sns.heatmap(data, annot=True,xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad=12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    plt.title(f"My Probability of Win(Tie) Scoring By Cards \n N = {num_decks}")

    # SCORING BY TRICKS
    tricks_scores = (p1_wins_by_trick/num_decks) * 100
    data = tricks_scores
    tricks_scores[tricks_scores == 0] = -1
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]

    plt.subplot(1, 2, 2)
    viz = sns.heatmap(data, annot=True, xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad = 12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    plt.title(f"My Probability of Win(Tie) Scoring By Tricks \n N = {num_decks}")
    plt.tight_layout()
    plt.show()
