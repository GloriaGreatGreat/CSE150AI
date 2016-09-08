# -*- coding: utf-8 -*-
__author__ = 'Yujia Li, Ze Li, Wei Wang'
__email__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

from collections import deque


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
   
    while len(queue_arcs) != 0:
        current = queue_arcs.pop()
        xi = current[0]
        xj = current[1]
        if revise(csp, xi, xj):
            if len(xi.domain) == 0: return False
            for xk in csp.constraints[xi]:
                if xk.var2 != xj: queue_arcs.append((xi, xk.var2))
    return True

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    return_bool = False
    for x in xi.domain:
        count = 0
        for y in xj.domain:
            for each in csp.constraints[xi,xj]:
                if each.is_satisfied(x,y): 
                    count = count + 1
        if count == 0:
            xi.domain.remove(x)
            return_bool = True
    return return_bool
