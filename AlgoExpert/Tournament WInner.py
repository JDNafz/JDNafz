'''
🟢 Easy Difficulty

https://www.algoexpert.io/questions/tournament-winner

'''

def tournamentWinner(competitions, results):
    scores = {}
    for i in range(len(competitions)):
        if results[i] == 1: #if home team won
            if competitions[i][0] in scores.keys():
                scores[competitions[i][0]] += 3
            else: 
                scores[competitions[i][0]] = 3 
        else: #Away team won 
            if competitions[i][1] in scores.keys():
                scores[competitions[i][1]] += 3     #add 3 to home team score
            else: #key:value doesn't exist yet> add it
                scores[competitions[i][1]] = 3 
    
    return max(scores, key=scores.get)
    
