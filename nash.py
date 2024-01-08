import nashpy as nash
import numpy as np
import matplotlib.pyplot as plt

def plot_strategy(d_strategy, w_strategy, eu_d, eu_w):
    fig, axes = plt.subplots(2, 2, sharey='row')
    x = np.arange(len(d_strategy))

    # Plot each vector as a bar chart in the subplots
    axes[0, 0].bar(x, d_strategy)
    axes[0, 0].set_title('Depositor\'s strategy')

    axes[0, 1].bar(x, w_strategy)
    axes[0, 1].set_title('Withdrawer\'s strategy')

    axes[1, 0].bar(x, eu_d)
    axes[1, 0].set_title('Depositor\'s Expected Payoff')

    axes[1, 1].bar(x, eu_w)
    axes[1, 1].set_title('Withdrawer\'s Expected Payoff')

    plt.tight_layout()
    plt.savefig("algo.png")

if __name__ == "__main__":
    payoff_depositor = []
    payoff_withdrawer = []
    size = 9
    for i in range(size):
        d = i + 1
        payoff_depositor.append([])
        payoff_withdrawer.append([])
        for j in range(size):
            w = j + 1
            if w <=d:
                payoff_depositor[i].append(d -w)
                payoff_withdrawer[i].append(w)
            else:
                payoff_depositor[i].append(d)
                payoff_withdrawer[i].append(0)
    # print(payoff_depositor)
    deposit_game = nash.Game(payoff_depositor, payoff_withdrawer)
    print(deposit_game)
    d_strategy, w_strategy = deposit_game.lemke_howson(initial_dropped_label =0)
    print(d_strategy, w_strategy)
    eu_depositor = np.matmul(payoff_depositor, w_strategy)
    eu_withdrawer = np.matmul(d_strategy, payoff_withdrawer)
    plot_strategy(d_strategy, w_strategy, eu_depositor, eu_withdrawer)
