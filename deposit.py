import matplotlib.pyplot as plt

def build_withdrawal_probablity():
    prob_sum = 0
    p = [0 for _ in range(1000)]
    for i in reversed(range(1000)):
        # i = 0, ...,999
        # d = 1, ..., 1000
        withdrawal = i + 1
        prob_sum += 1/withdrawal
        if prob_sum < 1:
            p[i] = 1/withdrawal
        else:
            p[i] = 1-sum(p)
            break
    return p


def payoff(p, d):
    expected_withdrawal = 0
    for i in range(d):
        withdrawal = i + 1
        expected_withdrawal += withdrawal * p[i]
    return d - expected_withdrawal

def plot_payoff(p):
    x = [i + 1 for i in range(1000)]
    y = [payoff(p, i + 1) for i in range(1000)]

    # Plot x against y
    plt.plot(x, y)

    # Customize the plot (optional)
    plt.xlabel('Deposit action')
    plt.ylabel('Payoff')
    plt.title('Depositor Mixed strategy')

    # Show the plot
    plt.savefig("deposit_payoff.png")
    plt.clf()

def plot_prob(p):
    x = [i + 1 for i in range(1000)]
    plt.bar(x, p)
    plt.xlabel('Withdraw action')
    plt.title('Withdrawer probability')
    # Show the plot
    plt.savefig("withdraw_prob.png")
    plt.clf()

if __name__ == "__main__":
    p = build_withdrawal_probablity()
    print(sum(p), len(p), p)

    # plot_payoff(p)
    # plot_prob(p)
    for i in range(1000):
        print(i+1, payoff(p, i + 1))