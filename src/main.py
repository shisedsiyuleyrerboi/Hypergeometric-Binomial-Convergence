import matplotlib.pyplot as plt
import math
import os

os.system('cls')

correct_selection = False
while (correct_selection != True): 
    N_min = int(input('Minimum # of Simulations(N) = '))
    N_max = int(input('Maximum # of Simulations(N) = '))
    n = 10
    k = int(input('# of Successes(k)           = '))
    print(f'Sample Space(n)             = {n}')

    if (k >= 0 and N_min > 0 and N_max >= N_min):
        correct_selection = True

# Case 1 (p = 0.3, r = pN)
def hypergeometric_function_case_1(N, n, k):
    p = 0.3
    r = int(round(p * N))
    if (k > r or (n-k) > (N-r) or n > N or k < 0 or k > n):
        return 0
    return (math.comb(r, k) * math.comb(N - r, n - k)) / math.comb(N, n)

def binomial_function_case_1(n, k):
    p = 0.3
    if (k < 0 or k > n):
        return 0
    return math.comb(n, k) * (p**k) * (1 - p) ** (n - k)

# Case 2 (r = 20, p = r/N)
def hypergeometric_function_case_2(N, n, k):
    r = 20
    if (k > r or (n-k) > (N-r) or n > N or k < 0 or k > n):
        return 0
    return (math.comb(r, k) * math.comb(N - r, n - k)) / math.comb(N, n)

def binomial_function_case_2(n, k, N):
    r = 20
    p = r / N
    if (k < 0 or k > n):
        return 0
    return math.comb(n, k) * (p**k) * (1 - p) ** (n - k)

# VISUALIZATION #
N_values = list(range(N_min, N_max + 1))

hyper_case1 = [hypergeometric_function_case_1(N, n, k) for N in N_values]
binom_case1 = [binomial_function_case_1(n, k)] * len(N_values)

hyper_case2 = [hypergeometric_function_case_2(N, n, k) for N in N_values]
binom_case2 = [binomial_function_case_2(n, k, N) for N in N_values]

fig, axes = plt.subplots(1, 2, figsize=(12,5))

# Case 1
axes[0].plot(N_values, hyper_case1, label="Hypergeometric", color="blue")
axes[0].plot(N_values, binom_case1, "--", label="Binomial", color="red")
axes[0].set_title(f"Case 1: Hypergeometric vs Binomial (k={k})")
axes[0].set_xlabel("N")
axes[0].set_ylabel(f"P(X={k})")
axes[0].legend()
axes[0].grid(True)

# Case 2
axes[1].plot(N_values, hyper_case2, label="Hypergeometric", color="green")
axes[1].plot(N_values, binom_case2, "--", label="Binomial", color="orange")
axes[1].set_title(f"Case 2: Hypergeometric vs Binomial (k={k})")
axes[1].set_xlabel("N")
axes[1].set_ylabel(f"P(X={k})")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
