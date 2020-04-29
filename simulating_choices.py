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

    if(plot):
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

if __name__ == "__main__":

    MODE = {0:"Car", 1:"PT", 2:"Slow"}
    ZONE = {0:"Zone 1", 1:"Zone 2"}

    orig_zone = 0
    dest_zone = 1

    mu = 0
    beta = 1

    print("\nValue of Ita: ")
    ita = gumbel_distrubution(mu, beta, count=1)
    print(ita)

    utility = get_utility()
    utility = [utility[mode][orig_zone][dest_zone] for mode in range(3)] + ita
   
    print("\nMaximum of the modes")
    max_u = np.amax(utility)
    print(max_u)
    index = np.where(utility == max_u)
    print(index[0][0])