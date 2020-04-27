#########
# LAB 1_ab
# SECTION 2.1 - UTILITY FUNCTION
#########

# Python Packages
import math
import numpy as np


def UtilityFunction(tt_car, c_car, tt_inv_pt, tt_wait_pt, c_pt, distance, N_employed, u_mode=1):
    """
    Calculates utility for modes car, pt and slow given input 
    of level of service variables and zone characteristics for a set of o-d pairs

    INPUT
        tt_car     : traveltime with car
        c_car      : cost of traveling with car
        tt_inv_pt  : in vehicle time with public transport
        tt_wait_pt : wait time for public transport
        c_pt       : cost of travelling with public transport
        distance   : travel distance
        N_employed : number of employees at a destination zone
        x          : vector with parameters
    
    OUTPUT
        V_car  : utility of car
        V_pt   : utility of pt
        V_slow : utility of slow
    """

    ## Zone Parameters
    THETA = 0.5

    ## Car Parameters
    ALPHA_CAR = 0.25        # [constant
    TRAVEL_TIME = -0.075    # [mins]
    COST_CAR = -.05         # [SEK]

    ## Transit Parameters
    IN_VEHICLE_TIME = -0.05 # [min]
    WAITING_TIME = -0.1     # [min]
    COST_TRANSIT = -0.05    # [SEK]

    ## Slow Parameters
    ALPHA_SLOW = 0          # [constant]
    DISTANCE = -0.4         # [km]

    # Utility of car
    V_car = ALPHA_CAR + TRAVEL_TIME*tt_car + COST_CAR*c_car + THETA*np.log(N_employed)
    try:
        V_car = V_car/u_mode
    except ZeroDivisionError:
        V_car = float("inf")

    # Utility of transit
    V_pt = IN_VEHICLE_TIME*tt_inv_pt + WAITING_TIME*tt_wait_pt + COST_TRANSIT*c_pt + THETA*np.log(N_employed)
    try:
        V_pt = V_pt/u_mode
    except ZeroDivisionError:
        V_pt = float("inf")

    # Utility of slow
    V_slow = ALPHA_SLOW + DISTANCE*distance + THETA*np.log(N_employed)
    try:
        V_slow = V_slow/u_mode
    except ZeroDivisionError:
        V_slow = float("inf")

    return (V_car, V_pt, V_slow) 



def get_utility(origin_zone=None, destination_zone=None, mode=None, u_mode=1, emp_change_z1=0, emp_change_z2=0, verbose=False):
    """
    Calculates utility for given mode travelling between the given origin 
    and destination zone

    INPUT
        mode             : mode of travel (car, public transport, slow)
        origin_zone      : staring zone of mode (zone 1 or zone 2)
        destination_zone : end zone of mode (zone 1 or zone 2)
        verbose          : present mode details on utility values
    
    OUTPUT
        utility : returns the utility of the mode for given origin
                  and destination zone  
    """
    ## Parameters
    # Service Matrix
    tt_car     = np.array([[ 9.8, 26.1], [26.0,  1.3]])
    cost_car   = np.array([[11.7, 31.0], [31.0, 11.5]])
    cost_pt    = np.array([[10.0, 10.0], [10.0,  5.0]])
    tt_inv_pt  = np.array([[ 9.8,  0.0], [ 0.0,  1.3]])
    tt_wait_pt = np.array([[10.0, 10.0], [10.0,  5.0]])
    distance   = np.array([[ 9.8, 26.1], [26.0,  1.3]])
    num_employ = np.array([[10_000+emp_change_z1, 15_000+emp_change_z2],
                           [10_000+emp_change_z1, 15_000+emp_change_z2]])


    utility = UtilityFunction(tt_car, cost_car, tt_inv_pt, tt_wait_pt, cost_pt, distance, num_employ, u_mode)

    if(verbose):
        print("------- Deterministic Mode Utility -------")
        print("\nUtility of Car:")
        print(utility[0])
        print("\nUtility of PT:")
        print(utility[1])
        print("\nUtility of Slow:")
        print(utility[2])

    if (mode==None) and (destination_zone==None) and (origin_zone==None):
        return utility
    elif (destination_zone==None) and (origin_zone==None):
        return utility[mode]
    else:
        return utility[mode][origin_zone][destination_zone]





if __name__ == "__main__":
    
    MODE = {0:"Car", 1:"PT", 2:"Slow"}
    ZONE = {0:"Zone 1", 1:"Zone 2"}

    ## Question 1
    # Utility of travelling with car from zone 1 to zone 2
    # Answer
    mode = 0
    orig_zone = 0
    dest_zone = 1
    print("\nUtility of travelling with '{}' from {} --> {}".format(MODE[mode], ZONE[orig_zone], ZONE[dest_zone]))
    print(get_utility(orig_zone, dest_zone, mode))

    ## Question 2
    # Utility of travelling with pt from zone 2 to zone 1
    # Answer
    # Answer
    mode = 1
    orig_zone = 1
    dest_zone = 0
    print("\nUtility of travelling with '{}' from {} --> {}".format(MODE[mode], ZONE[orig_zone], ZONE[dest_zone]))
    print(get_utility(orig_zone, dest_zone, mode))

    print("\nUtility of travelling with ALL ")
    get_utility(verbose=True)