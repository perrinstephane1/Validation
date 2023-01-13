from parcours_largeur import bfs

def predicate_finder(graph, predicate=lambda n: False):
    def check_predicate(s, n, a):
        # increment the count
        a[2] += 1
        # check predicate
        a[1] = predicate(n)
        #set the node that cheks teh predicate in the last field of the accumulator
        if a[1]:
            a[3]=n
        # return true if predicate is true - stop the traversal
        return a[1]
    return bfs(graph, [predicate, False, 0], f1=check_predicate)