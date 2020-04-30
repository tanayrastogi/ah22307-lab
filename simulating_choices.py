#########
# LAB 1_ab
# SECTION 2.4 - SIMULATING CHOICES
#########

# Python Packages
import numpy as np 
import matplotlib.pyplot as plt

# Local Packages
from utility_function import get_utility


def gumbel_distrubution(mu, beta, count, plot=False):
    s = np.random.gumbel(mu, beta, count)

    if(plot and isinstance(count, int)):
        _, bins, _ = plt.hist(s, 30, density=True)    
        plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
                * np.exp( -np.exp( -(bins - mu) /beta) ),
                linewidth=2, color='r')
        plt.grid()
        plt.title("Gumbel Distribution with Mean: {} and Variance: {}".format(mu, beta))
        plt.xlim(-20, 60)
        plt.ylim(0, 0.5)
    
        return (s, plt)
    else:
        return s

def model_sampling(num_samples, mu, beta, origin_zone=0, destination_zone=1):

    # Output
    max_U, max_indx = list(), list()

    # Deterministic utility
    V = get_utility()
    V = np.array([V[mode][origin_zone][destination_zone] for mode in range(3)]).reshape(3,1)

    # Generate 3xsample_count array for random varaible
    ita = gumbel_distrubution(mu, beta, count=(3, num_samples))

    # Utility value
    U = np.add(V, ita)

    # Max U values
    max_U = np.amax(U, axis=0)
    max_indx = np.argmax(U, axis=0)
    unique, count = np.unique(max_indx, return_counts=True)
    count_dict = dict(zip(unique, count))

    ## TEST
    i = 0
    for v in count_dict.values():
        i += v
    assert i == num_samples

    return (max_U, max_indx, count_dict)





if __name__ == "__main__":

    MODE = {0:"Car", 1:"PT", 2:"Slow"}
    ZONE = {0:"Zone 1", 1:"Zone 2"}

    orig_zone = 0
    dest_zone = 1

    mu = 0
    beta = 1

    number_of_samples = 1_00_000

    # V = get_utility()
    # print("Actual Utility value:")
    # print([V[mode][orig_zone][dest_zone] for mode in range(3)])

    # indx_list = list()
    # for itr in range(number_of_samples):
    #     # print("\n-------- ITR {} --------".format(itr))
    #     ita = gumbel_distrubution(mu, beta, count=3)
    #     # print("ITA Value: ", ita)
        
    #     # print("Utility for each mode: ")       
    #     utility = [V[mode][orig_zone][dest_zone] for mode in range(3)] + ita
    #     # print(utility)

    #     max_u = np.amax(utility)
    #     index = np.where(utility == max_u)
    #     # print("The maximum value is {} at index {}".format(max_u, index[0][0]))
    #     indx_list.append(index[0][0])
    
    # print("\nCount")
    # print(round(indx_list.count(0)/number_of_samples, 4))
    # print(round(indx_list.count(1)/number_of_samples, 4))
    # print(round(indx_list.count(2)/number_of_samples, 4))


    V = get_utility()
    V = np.array([V[mode][orig_zone][dest_zone] for mode in range(3)]).reshape(3,1)
    # print("\nDeterministic Utility")
    # print(V)

    s = np.random.gumbel(0, 1, (3, 10_00_000))
    # print("\nRandom value")
    # print(s)

    # print("\nUtility")
    U = np.add(V, s)
    # print(U)

    # print("\nMax Values")
    max_U = np.amax(U, axis=0)
    # print(max_U)
    # print("Index")
    max_indx = np.argmax(U, axis=0) 
    # print(max_indx)
    unique, count = np.unique(max_indx, return_counts=True)
    dict_coutnt = dict(zip(unique, count))
    print(dict_coutnt)
    i = 0
    for v in dict_coutnt.values():
        i += v
    print(i)