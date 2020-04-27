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
    [ Pr(j|i,m) ]

    INPUT
        v_zone : NxN matrix with utilities to travel between zone i and j 
    
    OUTPUT
        P_zone : NxN matrix with probability to choose zone j as destination
                 conditional on origin i and utility function given by V_zone
    """

    # Exonential utilitiy values for each mode for travelling from origin to destination zone
    # Exponential values
    exp     = np.exp(v_zone,  dtype=np.float)
    
    # Row Sum of exponential with origin 1 and 2 
    exp_sum_origin1 = np.sum(exp[0])
    exp_sum_origin2 = np.sum(exp[1])
    
    # Destination choice probabilities
    Pr_zone = np.array( [np.divide(exp[0], exp_sum_origin1), np.divide(exp[1], exp_sum_origin2)] ).reshape(2,2)

    return Pr_zone




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
    probalities = list()
    for mode in range(3):
        utility = get_utility(mode=mode)
        # Destination choice probability
        probalities.append(DestinationProbability(utility))

    if(verbose):
        print("------- Probalities Destination Choice -------")
        print("\nProbalities of Car:")
        print( np.around(probalities[0], decimals=3) )
        print("\nProbalities of PT:")
        print( np.around(probalities[1], decimals=3) )
        print("\nProbalities of Slow:")
        print( np.around(probalities[2], decimals=3) )
    
    #### TEST to make sure that the sum of probabilities is 1
    #### If not true will give assertion error
    for mode in range(3):
        sum_of_prob = np.sum(probalities[mode])
        col_sum_of_prob = np.sum(probalities[mode], axis=1)
        assert (2.0 == sum_of_prob).all()
        assert (np.ones((1,2)) == col_sum_of_prob).all()


    if (mode==None) and (destination_zone==None) and (origin_zone==None):
        return probalities
    elif (destination_zone==None) and (origin_zone==None):
        return probalities[mode]
    else:
        return probalities[mode][origin_zone][destination_zone]




def answer(ques=-1):

    MODE = {0:"Car", 1:"PT", 2:"Slow"}
    ZONE = {0:"Zone 1", 1:"Zone 2"}

    if ques == 1:
        ## Question 1
        # Probability for Destination Choice Model
        # Answer
        print("\nProbability of choosing destination for all modeL")
        get_probability(verbose=True)







if __name__ == "__main__":
    answer(1)

    
