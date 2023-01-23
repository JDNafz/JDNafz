'''
Algoexperts version of the stable marriage problem

🔵 Medium Difficulty

https://www.algoexpert.io/questions/stable-internships
'''

def stableInternships(interns, teams):
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0] * len(interns)
    
    teamMaps = []
    for team in teams:
        rank = {}
        print(team)
        for i, internNum in enumerate(team):
            rank[internNum] = i
        teamMaps.append(rank)
    print(teamMaps)

    while len(freeInterns) > 0:
        internNum = freeInterns.pop()

        intern = interns[internNum]
        teamPreference = intern[currentInternChoices[internNum]]
        currentInternChoices[internNum] += 1

        if teamPreference not in chosenInterns:
            chosenInterns[teamPreference] = internNum
            continue

        previousIntern = chosenInterns[teamPreference]
        previousInternRank = teamMaps[teamPreference][previousIntern]
        currentInternRank = teamMaps[teamPreference][internNum]

        if currentInternRank < previousInternRank:
            freeInterns.append(previousIntern)
            chosenInterns[teamPreference] = internNum
        else:
            freeInterns.append(internNum)
    
    matches = [[internNum, teamNum] for teamNum, internNum in chosenInterns.items()]
    return matches


interns = [[0, 1], [1, 0]]
teams = [[1, 0], [1, 0]]
stableInternships(interns, teams)