# CMPS 2200 Assignment 4
## Answers

**Name:** Cameron McLaren


Place all written answers from `assignment-04.md` here for easier grading.

1a) To produce as few coins as possible given N dollars, a largest denomination first greedy algorithm would work. Essentially, we take as many coins with the largest value possible. Once there's not enough left to keep using that coin denomination, we decrease to the next highest coin denomination. Then we keep doing this process until the exact amount is exchanged.

1b) Given optimal sequence of coins C, where C(i) is the number of coins with the denomination 2^i. Therefore, for all i < k, C(i) < 2. Then, for 2^k we just select as many coins as possible. This process represents the greedy algorithm described above, making it most optimal.

1c) The work and span of the algorithm is O(log(N)) since for each time we go to a smaller coin value, we reduce N faster than we reduce the number of coins of each denomination.

2a) Given we have coin denominations of 1, 5, and 8, and we want to make change for 20, the greedy algorithm would pick two 8 coins and four 1 coins, while the optimal solution is actually four 5 coins.

2b) C(N, i) is the minimum number of coins needed to make change for n.

2c) The work and span for the memoized approach is O(N*k) because the number of distinct subproblems is N*k
