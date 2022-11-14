'''
1. Everybody gets at least one rewards
2. Everybody must have more or less than the person next to them (according to unique score)

🔴 Hard
https://www.algoexpert.io/questions/min-rewards
'''

def minRewards(scores):
    rewards = [1 for _ in scores]
    for idx in range(1, len(scores)):
        if scores[idx - 1] < scores[idx]:
            rewards[idx] = rewards[idx - 1] + 1
    for idx in reversed(range(len(scores) -1 )):
        if scores[idx] > scores[idx + 1]:
            rewards[idx] = max(rewards[idx], rewards[idx +1] + 1)
    return sum(rewards)

# test1 = [8, 4, 2, 1, 3, 6, 7, 9, 5]
# minRewards(test1)