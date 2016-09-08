# -*- coding: utf-8 -*-
__author__ = 'Yujia Li, Ze Li, Wei Wang'
__email__ = 'yul200@ucsd.edu, zel014@ucsd.edu, wew026@ucsd.edu'

def is_complete(csp):
	"""Returns True when the CSP assignment is complete, i.e. all of the variables in the CSP have values assigned."""
	for var in csp.variables:
		if var.is_assigned() == False:
			return False
	return True

	

    # Hint: The list of all variables for the CSP can be obtained by csp.variables.
    # Also, if the variable is assigned, variable.is assigned() will be True.
    # (Note that this can happen either by explicit assignment using variable.assign(value),
    # or when the domain of the variable has been reduced to a single value.)
    # TODO implement this