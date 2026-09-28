import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def visualize(p1_wins_by_trick, p1_ties_by_trick, p1_wins_by_card, p1_ties_by_card, num_decks):

# SCORING BY CARDS
    plt.figure(figsize=(16, 8))
    cmap = sns.color_palette("rocket", as_cmap=True)
    cmap.set_bad("lightgray")
    cards_scores = (p1_wins_by_card/num_decks) * 100
    data = cards_scores
    np.fill_diagonal(cards_scores, np.nan)
    cards_combos = ["BBB","BBR","BRB","BRR","RBB","RBR","RRB","RRR"]
    plt.subplot(1, 2, 1)
    label_cards = np.array([[f"{win} ({tie})" for win, tie in zip(win_row, tie_row)]for win_row, tie_row in zip(p1_wins_by_card, p1_ties_by_card)])
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
    label_tricks = np.array([[f"{win} ({tie})" for win, tie in zip(win_row, tie_row)]for win_row, tie_row in zip(p1_wins_by_trick, p1_ties_by_trick)])
    viz = sns.heatmap(data, annot=label_tricks,fmt="", cmap=cmap,xticklabels = cards_combos, yticklabels=cards_combos,cbar=False)
    plt.ylabel("Opponent Choice", fontsize = 12, labelpad = 12)
    plt.xlabel("My Choice", fontsize = 12, labelpad = 12)
    plt.title(f"My Probability of Win(Tie) Scoring By Tricks \n N = {num_decks}")
    plt.tight_layout()
    plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")
    plt.show()
