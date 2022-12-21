# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/optimization.utils.ipynb (unless otherwise specified).

__all__ = ['get_selected_function_array', 'get_selected_function_ids', 'get_selected_functions_lm2']

# Cell
import itertools
import numpy as np

# Cell

def get_selected_function_array(replicates,d):

    p = replicates[0].results[1][0.].shape[1]
    nreps = len(list(replicates.keys()))

    selected_function_array = np.zeros(np.repeat(p,d))
    for r in range(nreps):
        sel_l = replicates[r].sel_l

        sel[r] = np.where((replicates[r].cs_reorder**2).sum(axis = tuple([1,2]))[sel_l] !=0.)[0]
        edit_locations = itertools.permutations(sel[r], d)
        for j in range(len(edit_locations)):
            selected_function_array[tuple(sel[r][edit_locations[j]] )] += 1

    return(selected_function_array)

# Cell

def get_selected_function_ids(replicates, d):

    nreps = len(list(replicates.keys()))

    selected_function_ids = np.zeros((nreps,d))
    for r in range(nreps):
        sel_l = replicates[r].sel_l
        selected_function_ids[r] = np.where((replicates[r].cs_reorder**2).sum(axis = tuple([1,2]))[sel_l] !=0.)[0]
    return(selected_function_ids)

# Cell
def get_selected_functions_lm2(replicates):

    nreps = len(list(replicates.keys()))

    selected_function_ids = {}
    for r in range(nreps):
        sel_l = 1
        selected_function_ids[r] = np.where((replicates[r].cs_reorder**2).sum(axis = tuple([1,2]))[sel_l] !=0.)[0]

    return(selected_function_ids)