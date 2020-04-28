# Python Import
import streamlit as st
import pandas as pd

# Local Imports
from utility_function import get_utility


# Global Constants
MODE = {"Car":0, "PT":1, "Slow":2}
ZONE = {"Zone 1":0, "Zone 2":1}


def presentation():
    st.markdown("## 2.1 Utility Function")
    # Show Utility Matrix
    if st.checkbox("Show Utility Matrixes"):
        utilities = get_utility()
        st.markdown("Utility for **CAR**")
        st.dataframe(pd.DataFrame(utilities[0], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Utility for **PUBLIC TRANSPORT (PT)**")
        st.dataframe(pd.DataFrame(utilities[1], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Utility for **SLOW**")
        st.dataframe(pd.DataFrame(utilities[2], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))



    # ------------------------- Write Up for the section ------------------------- #
    # ---------------------------------------------------------------------------- #
    st.markdown("""
    ## Utility Function
    For the lab we assume that there are three alternate modes of transportation, *m*, that can travel between two zones, *i* and *j*. The utilities of each alternative are defined by, 
    """)
    st.latex(r'''
    V_{j,car}^i = \alpha_{car} + \beta_{car}t_{j,car}^i + \gamma_{car}c_{j,car}^i+\theta\ln(N_{employed}^j) 
    ''')
    st.latex(r'''
    V_{j,pt}^i = \beta_{inv}t_{j,inv}^i + \beta_{wait}t_{j,wait}^i + \gamma_{pt}c_{j,pt}^i+\theta\ln(N_{employed}^j)
    ''')
    st.latex(r'''
    V_{j,slow}^i = \alpha_{slow} + \phi d_{ij} + \theta\ln(N_{employed}^j)
    ''')
    st.markdown("""
    where,      
    -   $t_{j,car}^i$ = travel time by car from zone *i* to *j*
    -   $c_{j,car}^i$ = cost of traveling by car from zone *i* to *j* 
    -   $t_{j,inv}^i$ = in-vehicle travel time by pt from zone *i* to *j*
    -   $t_{j,wait}^i$ = waiting time for of traveling by pt from zone *i* to *j*
    -   $c_{j,pt}^i$ = cost of traveling by pt from zone *i* to *j*
    -   $d_{ij}$ = distance between zone *i* and *j*
    -   $N_{employed}^j$ = number of employee in zone *j*
    """)

    st.write("")
    st.markdown("""
    The model parameters are given by, 

    |      	| Variabe               	| Parameter       	|
    |------	|-----------------------	|-----------------	|
    | Zone 	| Size parameter        	| $\\theta$        	|
    | Car  	| ASC                   	| $\\alpha_{car}$  	|
    |      	| travel time (min)     	| $\\beta_{car}$   	|
    |      	| cost (SEK)            	| $\\gamma_{car}$  	|
    | PT   	| in-vehicle time (min) 	| $\\beta_{inv}$   	|
    |      	| waiting time (min)    	| $\\beta_{wait}$  	|
    |      	| cost (SEK)            	| $\\gamma_{pt}$   	|
    | Slow 	| ASC                   	| $\\alpha_{slow}$ 	|
    |      	| distance (km)         	| $\\phi$           	|
    """)

    # ------------------------------------ EXERCISES ------------------------------#
    # ---------------------------------------------------------------------------- #
    st.markdown("## EXCERCISES")
        
    if st.checkbox("(i)/(ii) Utilities of each mode given zone"):
        orig_zone = st.radio("Select Origin Zone", list(ZONE.keys()))
        dest_zone = st.radio("Select Destination Zone", list(ZONE.keys()))
        mode      = st.radio("Select Mode", list(MODE.keys()))
        utility = get_utility(ZONE[orig_zone], ZONE[dest_zone], MODE[mode])
        st.markdown("The utility of **{}** from **{}** to **{}** is given by,".format(mode, orig_zone, dest_zone))
        st.markdown("$V(m, i, j)$ = {}".format(round(utility, 4)))