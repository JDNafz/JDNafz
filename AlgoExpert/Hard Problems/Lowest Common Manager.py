'''
🔴 Hard

https://www.algoexpert.io/questions/lowest-common-manager
'''
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
        
class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numImportantReports)




# Test
A = OrgChart("A")
B = OrgChart("B")
C = OrgChart("C")
D = OrgChart("D")
E = OrgChart("E")
F = OrgChart("F")
G = OrgChart("G")
H = OrgChart("H")
I = OrgChart("I")

A.directReports.append(B)
A.directReports.append(C)

B.directReports.append(D)
B.directReports.append(E)

C.directReports.append(F)
C.directReports.append(G)

D.directReports.append(H)
D.directReports.append(I)

print(getLowestCommonManager(A, E, I).name)
