import matplotlib.pyplot as plt
import numpy as np
import math
import os

os.system('cls')

correct_selection = False
while (correct_selection != True):
    N_min = int(input('Minimum # of Simulations(N) = '))
    N_max = int(input('Maximum # of Simulations(N) = '))
    n = 10
    k = 10

    if (N_min > 0 and N_max > N_min):
        correct_selection = True

# Case 1 (p = 0.3, r = pN)
def hypergeometric_function_case_1(N, n, k):
    p = 0.3
    r = int(p * N)
    return (math.comb(r, k) * math.comb(N - r, n - k)) / math.comb(N, n)

def binomial_function_case_1(n, k):
    p = 0.3
    return math.comb(n, k) * (p**k) * (1 - p) ** (n - k)

# Case 2 (r = 20, p = r/N)
def hypergeometric_function_case_2(N, n, k):
    r = 20
    return (math.comb(r, k) * math.comb(N - r, n - k)) / math.comb(N, n)

def binomial_function_case_2(n, k, N):
    r = 20
    p = r / N
    return math.comb(n, k) * (p**k) * (1 - p) ** (n - k)

# VISUALIZATION #
x = np.arange(0, n+1)
N_values = np.linspace(N_min, N_max, 4, dtype=int)

plt.figure(figsize=(14,16))

# Case 1
for i, N in enumerate(N_values, 1):
    prob_hypergeo = [hypergeometric_function_case_1(N, n, k) for k in x]
    prob_binomial = [binomial_function_case_1(n, k) for k in x]

    plt.subplot(4,2,i)
    plt.bar(x-0.2, prob_binomial, width=0.4,
            label=f"Binomial(n={n}, p=0.3)", alpha=0.7)
    plt.bar(x+0.2, prob_hypergeo, width=0.4,
            label=f"Hypergeo(N={N}, r={int(0.3*N)}, n={n})", alpha=0.7)
    plt.title(f"Case 1: Hypergeo vs Binomial (N={N})")
    plt.xlabel("k (número de éxitos)")
    plt.ylabel("Probabilidad")
    plt.legend()

# Case 2
for j, N in enumerate(N_values, 1):
    prob_hypergeo = [hypergeometric_function_case_2(N, n, k) for k in x]
    prob_binomial = [binomial_function_case_2(n, k, N) for k in x]

    plt.subplot(4,2,4+j)
    plt.bar(x-0.2, prob_binomial, width=0.4,
            label=f"Binomial(n={n}, p={20/N:.3f})", alpha=0.7)
    plt.bar(x+0.2, prob_hypergeo, width=0.4,
            label=f"Hypergeo(N={N}, r=20, n={n})", alpha=0.7)
    plt.title(f"Case 2: Hypergeo vs Binomial (N={N})")
    plt.xlabel("k (número de éxitos)")
    plt.ylabel("Probabilidad")
    plt.legend()

plt.tight_layout()
plt.show()
