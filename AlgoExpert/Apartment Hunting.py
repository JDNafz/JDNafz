'''
Find the distance in blocks from the given community ammenities,
find the location with the fewest blocks to any given ammenity.

⚫ Very Hard
https://www.algoexpert.io/questions/apartment-hunting
'''
def apartmentHunting(blocks, reqs):
    #requisit_Distances (reqDs)
    reqDs = [apt for apt in blocks]
    for apt in range(len(blocks)):
        for req in reqs:
            if blocks[apt][req] == True:
                reqDs[apt][req] = 0
            elif blocks[apt][req] == False:
                if apt == 0:
                    reqDs[apt][req] = float('inf')
                    continue
                else:
                    reqDs[apt][req] = reqDs[apt - 1][req] + 1

    for apt in range(len(blocks) -1, 0, -1):
        for req in reqs:
            if reqDs[apt - 1][req] > reqDs[apt][req]:
                reqDs[apt - 1][req] = reqDs[apt][req] + 1

    total = [ float('-inf') for _ in reqDs]
    for apt in range(len(reqDs)):
        maxList = []
        for req in reqDs[apt]:
            if reqDs[apt][req] == 'True' or reqDs[apt][req] == 'False':
                continue
            else:
                maxList.append(reqDs[apt][req])
        total[apt] = max(maxList)
        maxList = []
        
    bestplace = min(total)
    for idx in range(len(total)):
        if total[idx] == bestplace:
            print("FINAL:",idx)
            return idx


# def pprint(dictlist):
#     for dict in dictlist:
#         print(dict)


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

blocks4 = [
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
reqs4 = ["gym", "school", "store"]
# apartmentHunting(blocks2,reqs2)

blocks6 = [
    {
      "gym": True,
      "pool": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": False,
      "store": True
    },
    {
      "gym": True,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": False,
      "store": False
    },
    {
      "gym": False,
      "pool": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "pool": True,
      "school": False,
      "store": False
    }
  ]
reqs6 = ["gym", "pool", "school", "store"]
# apartmentHunting(blocks6,reqs6)

