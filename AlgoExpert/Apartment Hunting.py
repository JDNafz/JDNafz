def apartmentHunting(blocks, reqs):
    # print(blocks[0]['gym'])

    #requisit_Distances (reqDs)
    reqDs = [apt for apt in blocks]
    for apt in range(len(blocks)):
        for req in blocks[apt]:
            if blocks[apt][req] == True:
                reqDs[apt][req] = 0
            elif blocks[apt][req] == False:
                if apt == 0:
                    reqDs[apt][req] = float('inf')
                    continue
                else:
                    reqDs[apt][req] = reqDs[apt - 1][req] + 1
    # print("First Run:")
    # pprint(reqDs)

    for apt in range(len(blocks) -2, -1, -1):
        # print(apt)
        for req in blocks[apt]:
            if reqDs[apt][req] == float('inf'):
                reqDs[apt][req] = reqDs[apt + 1][req] + 1

    # print("Second Run:")
    pprint(reqDs)
    total = [ float('-inf') for _ in reqDs]
    for apt in range(len(reqDs)):
        maxList = []
        for req in reqDs[apt]:
            maxList.append(reqDs[apt][req])
        total[apt] = max(maxList)
        maxList = []
        
    print(total)
    bestplace = min(total)
    for idx in range(len(total)):
        if total[idx] == bestplace:
            print("FINAL:",idx)
            return idx

 
# def minRewards(scores):
#     rewards = [1 for _ in scores]
#     for idx in range(1, len(scores)):
#         if scores[idx - 1] < scores[idx]:
#             rewards[idx] = rewards[idx - 1] + 1
#     for idx in reversed(range(len(scores) -1 )):
#         if scores[idx] > scores[idx + 1]:
#             rewards[idx] = max(rewards[idx], rewards[idx +1] + 1)
#     return sum(rewards)


def pprint(dictlist):
    for dict in dictlist:
        print(dict)




blocks = [
  { "gym": False,
    "school": True,
    "store": False   },

  { "gym": True,
    "school": False,
    "store": False  },

  { "gym": True,
    "school": True,
    "store": False },

  { "gym": False,
    "school": True,
    "store": False },

  { "gym": False,
    "school": True,
    "store": True   }
]
reqs = ["gym", "school", "store"]
# apartmentHunting(blocks, reqs)

blocks2 = [
    {
      "foo": True,
      "gym": False,
      "kappa": False,
      "office": True,
      "school": True,
      "store": False
    },
    {
      "foo": True,
      "gym": True,
      "kappa": False,
      "office": False,
      "school": False,
      "store": False
    },
    {
      "foo": True,
      "gym": True,
      "kappa": False,
      "office": False,
      "school": True,
      "store": False
    },
    {
      "foo": True,
      "gym": False,
      "kappa": False,
      "office": False,
      "school": True,
      "store": False
    },
    {
      "foo": True,
      "gym": True,
      "kappa": False,
      "office": False,
      "school": True,
      "store": False
    },
    {
      "foo": True,
      "gym": False,
      "kappa": False,
      "office": False,
      "school": True,
      "store": True
    }
  ]
reqs2 = ["gym", "school", "store"]
apartmentHunting(blocks2,reqs2)
