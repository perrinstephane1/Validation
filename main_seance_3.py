from seance_2.HanoiConfiguration import HanoiConfiguration
from seance_3.ParentTraceProxy import ParentTraceProxy
from seance_3.IdentityProxy import *
from seance_1.predicate_finder import predicate_finder
from seance_3.ParentTraceProxy import *
from seance_2.HanoiGraph import *

def predic(source):
    return source.hanoi_on_entry(source)

def testGetTrace():
    dict = {1: 1, 2: 1, 3: 1, 5: 2, 6: 2, 4: 5}
    print(getTrace(dict, 6))

def printDict(dict, i):
    print("{} : {}".format(i.conf, dict[i].conf))

def testRecherche(dict, target):
    res=[]
    temoin=target
    for k in range(10):
        printDict(dict, temoin)
        temoin=dict[temoin]




if __name__ == '__main__':
    h = HanoiConfiguration(3, 3)
    hg=HanoiGraph(h)
    pDict = {}
    ptp = ParentTraceProxy(hg, pDict)
    [p, found, count, target], known = predicate_finder(ptp, hg.hanoi_on_entry1)
    #testRecherche(pDict, target)
    #print(hg == hg)
    #print(target.conf)
    print(getTrace(pDict, target))
    # getTrace(pDict, target)
