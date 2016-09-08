# -*- coding: utf-8 -*-
__author__ = 'Yujia Li, Ze Li, Wei Wang'
__email__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'


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
    