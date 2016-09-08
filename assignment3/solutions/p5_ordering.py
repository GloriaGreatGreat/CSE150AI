# -*- coding: utf-8 -*-
__author__ = 'Yujia Li, Ze Li, Wei Wang'
__email__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'


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
