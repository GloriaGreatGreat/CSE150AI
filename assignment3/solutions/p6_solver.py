# -*- coding: utf-8 -*-
__author__ = 'Yujia Li, Ze Li, Wei Wang'
__email__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

from collections import deque


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())
    #return True

def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None

def is_complete(csp):
    """Returns True when the CSP assignment is complete, i.e. all of the variables in the CSP have values assigned."""
    for var in csp.variables:
        if var.is_assigned() == False:
            return False
    return True

def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""

    for cons in csp.constraints[variable]:
        check_var = None
        if cons.var1.name == variable.name:
            check_var = cons.var2
        else: check_var = cons.var1
        if(check_var.is_assigned() == True):
            variable.assign(value)
            if cons.is_satisfied(value,check_var.value) == False: return False
    return True
    # TODO implement this

def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns the successful assignment; otherwise, it returns None.
    """
    if is_complete(csp):return csp 
    var = select_unassigned_variable(csp);
    for value in order_domain_values(csp, var):
        if is_consistent(csp, var, value):
            csp.variables.begin_transaction()
            csp.assignment[var] = value
            var.assign(value)
            if backtrack(csp): 
                return csp       
            csp.variables.rollback()
    return None  


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


def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """
    # return next((variable for variable in csp.variables if not variable.is_assigned()))
    count = float("infinity")
    for variable in csp.variables:
        if variable.is_assigned() == False:
            number = len(variable.domain)
            if number < count:
                count = number
                use = variable
            if number == count:
                use = compare(use, variable, csp)
    return use

def compare(use, variable, csp):
    use_number = 0
    variable_number = 0
    for cons in csp.constraints:
        if cons.var1 == use and cons.var2.is_assigned == False or cons.var2 == use and cons.var1.is_assigned == False:
            use_number = use_number + 1
    for cons2 in csp.constraints:
        if cons.var1 == variable and cons2.var2.is_assigned == False or cons.var2 == variable and cons2.var1.is_assigned == False:
            variable_number = variable_number + 1
    if use_number > variable_number: 
        return use
    else:
        return variable


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the values are
    ordered in the increasing order of the number choices for the neighboring variables in the constraint graph
    """

    # TODO implement this
    store = []
    constraint_list = csp.constraints[variable]
    for value in variable.domain:
        count = 0
        for current_neighbor in constraint_list:
            for neighbor_var in current_neighbor.var2.domain:
                if current_neighbor.is_satisfied(value, neighbor_var):
                    count = count + 1
        store.append((value, -count))
    store = sorted(store, key = getKey)
    #print(store)
    return_list = []
    for var in store:
        return_list.append(var[0])
    return return_list

def getKey(item):
    return item[1]
