#########
# LAB 1_ab
# SECTION 2.2  - MODE CHOICE MODEL
#########

# Python Packages
import math
import numpy as np 

# Local Imports
from utility_function import get_utility


def ModeProbability(v_car, v_pt, v_slow):
    """
    Calculates logit choice probabilities of modes car, pt and slow
    given input utilities respectively

    INPUT
        v_car  : utility of car
        v_pt   : utility of pt
        v_slow : utility of slow
    
    OUTPUT
        P_car  : probability of car
        P_pt   : probability of pt
        P_slow : probability of slow
    """

    # Exonential utilitiy values for each mode for travelling from origin to destination zone
    # Exponential values
    exp_car  = np.exp(v_car,  dtype=np.float)
    exp_pt   = np.exp(v_pt,   dtype=np.float)
    exp_slow = np.exp(v_slow, dtype=np.float)

    exp_sum = exp_car + exp_pt + exp_slow

    # Probabilites of each mode
    Pr_car  = np.divide(exp_car,  exp_sum, dtype=np.float)
    Pr_pt   = np.divide(exp_pt,   exp_sum, dtype=np.float)
    Pr_slow = np.divide(exp_slow, exp_sum, dtype=np.float)

    return (Pr_car, Pr_pt, Pr_slow)


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
    utility = get_utility(u_mode = u_mode, emp_change_z1=emp_change_z1, emp_change_z2=emp_change_z2)
    # Probabilitiy values for each mode of travelling from origin to destination zone
    probalities = ModeProbability(utility[0], utility[1], utility[2])

    if(verbose):
        print("------- Probalities Mode Utility -------")
        print("\nProbalities of Car:")
        print( np.around(probalities[0], decimals=3) )
        print("\nProbalities of PT:")
        print( np.around(probalities[1], decimals=3) )
        print("\nProbalities of Slow:")
        print( np.around(probalities[2], decimals=3) )
    
    #### TEST to make sure that the sum of probabilities is 1
    #### If not true will give assertion error
    sum_of_prob = probalities[0] + probalities[1] + probalities[2]
    sum_of_prob = np.around(sum_of_prob, decimals = 5)
    assert (np.ones((2,2)) == sum_of_prob).all()

    if mode == None:
        return probalities
    else:
        return probalities[mode][origin_zone][destination_zone]





def answer(ques=-1):

    MODE = {0:"Car", 1:"PT", 2:"Slow"}
    ZONE = {0:"Zone 1", 1:"Zone 2"}

    if ques == 1:
        ## Question 1
        # Probability for Mode Choice Model
        # Answer
        print("\nProbability of travelling with ALL")
        get_probability(verbose=True)

    elif ques == 2:
        ## Question 2
        # Probability of travelling with car from zone 1 to zone 2
        # Answer
        mode = 0
        orig_zone = 0
        dest_zone = 1
        print("\nProbability of travelling with '{}' from {} --> {}".format(MODE[mode], ZONE[orig_zone], ZONE[dest_zone]))
        print(get_probability(orig_zone, dest_zone, mode))

    elif ques == 3:
        ## Question 3
        # Probability of travelling with car to any destination 
        # Answer
        # MODE: CAR
        mode = 0
        # ZONE: ZONE 1 --> ZONE 2
        orig_zone = 0
        dest_zone = 1
        zone12 = get_probability(orig_zone, dest_zone, mode)
        # ZONE: ZONE 2 --> ZONE 1
        orig_zone = 1
        dest_zone = 0
        zone21 = get_probability(orig_zone, dest_zone, mode)
        print("\nProbability of travelling with '{}' from any zone".format(MODE[mode]))
        print(zone12*0.5 + zone21*0.5)


    elif ques == 4:
        ## Question 4
        # Probability for Mode Choice Model with u_mode 10
        # Answer
        print("\nProbability of travelling with ALL with u_mode 1")
        get_probability(u_mode = 1, verbose=True)
        print("\nProbability of travelling with ALL with u_mode 10")
        get_probability(u_mode = 10, verbose=True)
        print("\nProbability of travelling with ALL with u_mode 0.1")
        get_probability(u_mode = 0.1, verbose=True)
    

    elif ques == 5:
        ## Question 5
        # Probability for Mode Choice Model
        # Answer
        print("\nProbability of travelling with ALL")
        get_probability(verbose=True)
        print("\nProbability of travelling with ALL with 1000 MORE employess in each zone")
        get_probability(emp_change_z1=0, emp_change_z2=1000, verbose=True)
        print("\nProbability of travelling with ALL with 1000 LESS employess in each zone")
        get_probability(emp_change_z1=5000, emp_change_z2=-1000, verbose=True)



    
    else:
        print("Choose correct option")





if __name__ == "__main__":

    answer(5)





