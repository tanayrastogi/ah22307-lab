#########
# LAB 1_ab
# SECTION 2.3  - DESTINATION CHOICE MODEL
#########

# Python Packages
import math
import numpy as np

# Local Imports
from utility_function import get_utility


def DestinationProbability(v_zone):
    """
    Calculates logit choice probabilities for choosing a specific destination 
    j conditional to origin i when the utility of travelling between zone i and j 
    is given by v_zone

    INPUT
        v_zone : NxN matrix with utilities to travel between zone i and j 
    
    OUTPUT
        P_zone : NxN matrix with probability to choose zone j as destination
                 conditional on origin i and utility function given by V_zone
    """

    print(v_zone)
    pass




def get_probability(origin_zone=None, destination_zone=None, mode=None, u_mode=1, emp_change_z1=0, emp_change_z2=0, verbose=False):
    """
    Gives probaility of choosing a mode for someone travelling from 
    given origin zone to destination zone

    INPUT
        mode             : mode of travel (car, public transport, slow)
        origin_zone      : staring zone of mode (zone 1 or zone 2)
        destination_zone : end zone of mode (zone 1 or zone 2)
        verbose          : present mode details on utility values
    
    OUTPUT
        probabilities    : returns the probaility for choosing the mode for given origin
                           and destination zone  
    """

    # Utilitiy values for each mode of travelling from origin to destination zone
    utility = get_utility(origin_zone=origin_zone,
                          destination_zone=destination_zone,
                          mode=mode)
    return utility


if __name__ == "__main__":
        
    MODE = {0:"Car", 1:"PT", 2:"Slow"}
    ZONE = {0:"Zone 1", 1:"Zone 2"}

    mode = 0
    orig_zone = 0
    dest_zone = 1
    print("\nProbability of travelling with '{}' from {} --> {}".format(MODE[mode], ZONE[orig_zone], ZONE[dest_zone]))
    print(get_probability(origin_zone=orig_zone,
                          destination_zone=dest_zone,
                          mode=mode))
    
    
