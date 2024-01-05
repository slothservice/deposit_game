import matplotlib.pyplot as plt

def build_deposit_probablity():    
    q = [0 for _ in range(1000)]
    # initialize the last prob as 1
    q[999] = 1.0
    prob_sum = q[999]
    for i in reversed(range(368, 999)):
        # i = 368, ...,998
        withdraw = i + 1
        q[i] = 1/withdraw * prob_sum
        prob_sum += q[i]
    # normalize q
    prob_sum = sum(q)
    q_normalized = [weight/prob_sum for weight in q]
    return q_normalized


def payoff(p, w):
    return w * sum([p[i] for i in range(w - 1, 1000)])

def plot_payoff(p):
    x = [i + 1 for i in range(1000)]
    y = [payoff(p, i + 1) for i in range(1000)]

    plt.plot(x, y)
    plt.xlabel('Withdrawal action')
    plt.ylabel('Payoff')
    plt.title('Withdrawer Mixed strategy')

    # Show the plot
    plt.savefig("withdrawer_payoff.png")
    plt.clf()

def plot_prob(p):
    x = [i + 1 for i in range(1000)]
    plt.plot(x, p)
    plt.xlabel('Deposit action')
    plt.title('Deposit probability')
    # Show the plot
    plt.savefig("deposit_prob.png")
    plt.clf()


if __name__ == "__main__":
    p = build_deposit_probablity()
    print(sum(p), len(p), p)
    # plot_prob(p)
    # plot_payoff(p)
