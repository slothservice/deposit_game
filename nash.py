import nashpy as nash
import numpy as np

if __name__ == "__main__":
    payoff_depositor = []
    payoff_withdrawer = []
    size =5
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