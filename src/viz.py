import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def visualize(p1_wins, num_decks):

# SCORING BY CARDS
    cards_scores = p1_wins
    data = cards_scores
    cards_scores[cards_scores == 0] = -1
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]
    plt.subplot(1, 2, 1)
    viz = sns.heatmap(data, annot=True,xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad=12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    plt.title(f"My Probability of Win(Tie) Scoring By Cards \n N = {num_decks}")

    # SCORING BY TRICKS
    tricks_scores = np.random.randint(1, 10,(8,8))
    data = tricks_scores
    tricks_scores[tricks_scores == 0] = -1
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]

    plt.subplot(1, 2, 2)
    viz = sns.heatmap(data, xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad = 12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    plt.title(f"My Probability of Win(Tie) Scoring By Tricks \n N = {num_decks}")
    plt.tight_layout()
    plt.show()
