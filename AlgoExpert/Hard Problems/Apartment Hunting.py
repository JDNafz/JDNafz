def apartmentHunting(blocks, reqs):
    # print(blocks[0]['gym'])

  
    reqsDistance = [apt for apt in blocks]
    for apt in range(1, len(blocks)):
        # print("Apt:", apt)
        for req in blocks[apt]:
            if blocks[apt][req] == True:
                reqsDistance[apt][req] = 0
            elif blocks[apt][req] == False:
                if reqsDistance[apt][req-1] == 69: #temp
                    reqsDistance[apt][req] = float('inf')
    pprint(reqsDistance)

    # test = '\t'.join([str(x) for x in reqsDistance])
    # print(test)

def pprint(dictlist):
    for dict in dictlist:
        print(dict)


    #     for key,value in dict.items():
    #         formatted = [key,value]
    #         for ele in formatted:
    #             templist.append(ele)
    #         # print(formatted, sep='\t')
    #         # templist.append('\t'.join(key + str(value)))
    # print(templist, sep='\t')


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
apartmentHunting(blocks, reqs)

