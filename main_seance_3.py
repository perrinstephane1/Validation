from seance_2.HanoiConfiguration import HanoiConfiguration
from seance_3.ParentTraceProxy import ParentTraceProxy
from seance_1 import predicate_finder
from seance_3.ParentTraceProxy import *

def testGetTrace():
    dict = {1: 1, 2: 1, 3: 1, 5: 2, 6: 2, 4: 5}
    print(getTrace(dict, 6))

if __name__ == '__main__':
    # h = HanoiConfiguration(3, 3)
    # pDict = {}
    # ptp = ParentTraceProxy(h, pDict)
    # [p, found, count, target] = predicate_finder(ptp, solution_pred)
    # getTrace(pDict, target)


