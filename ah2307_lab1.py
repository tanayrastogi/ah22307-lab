# Python Imports
import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.graph_objects as go

# Local Imports
from utility_function import get_utility
from mode_probability import get_probability

# Global Constants
MODE = {"Car":0, "PT":1, "Slow":2}
ZONE = {"Zone 1":0, "Zone 2":1}


def utility_function():
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



    # Text
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

    st.markdown("""

    The model parameters are given by, 

    |      	| Variabe               	| Parameter       	|
    |------	|-----------------------	|-----------------	|
    | Zone 	| Size parameter        	| $\\theta$        	|
    | Car  	| ASC                   	| $\\alpha_{car}$  	|
    |      	| travel time (min)     	| $\\beta_{car}$   	|
    |      	| cost (SEK)            	| $\gamma_{car}$  	|
    | PT   	| in-vehicle time (min) 	| $\\beta_{inv}$   	|
    |      	| waiting time (min)    	| $\\beta_{wait}$  	|
    |      	| cost (SEK)            	| $\gamma_{pt}$   	|
    | Slow 	| ASC                   	| $\\alpha_{slow}$ 	|
    |      	| distance (km)         	| $\phi$           	|
    """)

    # Show by Zone and Mode
    st.markdown("## EXCERCISES")
    if st.checkbox("(i)/(ii) Utilities of each mode given zone"):
        orig_zone = st.radio("Select Origin Zone", list(ZONE.keys()))
        dest_zone = st.radio("Select Destination Zone", list(ZONE.keys()))
        mode      = st.radio("Select Mode", list(MODE.keys()))
        utility = get_utility(ZONE[orig_zone], ZONE[dest_zone], MODE[mode])
        st.markdown("The utility of **{}** from **{}** to **{}** is given by,".format(mode, orig_zone, dest_zone))
        st.markdown("$V(m, i, j)$ = {}".format(round(utility, 4)))













def mode_choice_model():
    st.markdown("## 2.2 Mode Choice Model")

    # Show Probability Matrix
    if st.checkbox("Show Probability Matrixes"):
        probabilities = get_probability()
        st.markdown("Probability for **CAR**")
        st.write(pd.DataFrame(probabilities[0], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Probability for **PUBLIC TRANSPORT (PT)**")
        st.write(pd.DataFrame(probabilities[1], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Probability for **SLOW**")
        st.write(pd.DataFrame(probabilities[2], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))

    st.markdown("""
    ## Mode Choice Model
    The model calculates the probability of each alternative mode of transport given the origin and destination. 
    Hence, we calculate **$Pr(m|i,j)$**, where $m$ is mode and $i$ and $j$ are the origin and destination zones.
    """)    
    st.write("""
    Assuming the utility of choosing the alternative is given by, 

    $$
    U_{j,m}^i = V_{j,m}^i + \epsilon_{j,m}^i  
    $$

    where, $\epsilon_{j,m}^i$ is I.I.D Gumble distributed error term representing uncertinity. 
    """)
    st.write("""
    The probability that the utility for alternative $m$ given $i$ and $j$ is given by, 

    $$
    Pr(m|i,j) = Pr(U_{j,m}^i > U_{j,m'}^i) = \dfrac{\exp^{V_{j,m}^i}}{ \sum_{m'={1,2,3}} \exp^{V_{j,m'}^i} }
    $$
    """)

    
    # Show by Zone and Mode
    st.markdown("## EXERCISES")

    if st.checkbox("(ii) Probabilites of each zone given mode"):
        orig_zone = st.radio("Select Origin Zone", list(ZONE.keys()))
        dest_zone = st.radio("Select Destination Zone", list(ZONE.keys()))
        mode      = st.radio("Select Mode", list(MODE.keys()), key=1)
        probability = get_probability(ZONE[orig_zone], ZONE[dest_zone], MODE[mode])
        st.markdown("The probability of travelling from **{}** to **{}** using a **{}** is,".format(orig_zone, dest_zone, mode))
        st.markdown("$P(m|i,j)$ = **{}**".format(round(probability, 4)))


    if st.checkbox("(iii) Probability of travelling using choosen mode from zone 1 to any destination"):
        st.write("""
        Using the law of large numbers, 

        $$
        Pr(m|i) = \sum_{j={1,2}} Pr(m|i,j)*P(j)
        $$

        where, $P(j)$ is 0.5 for each zone and $i = 1$
        """)
        
        mode      = st.radio("Select Mode", list(MODE.keys()), key=2)
        zone11    = get_probability(ZONE["Zone 1"], ZONE["Zone 1"], MODE[mode])
        zone12    = get_probability(ZONE["Zone 1"], ZONE["Zone 2"], MODE[mode])
        
        st.markdown("The probability of travelling from **Zone 1** using **{}** is,".format(mode))
        st.markdown("$P(m|i=1)$ = **{}**".format(round(zone11*0.5 + zone12*0.5, 4)))



    if st.checkbox("(iv) Effect on probabilites choosing u_mode"):
        st.markdown("""
        Let us assume that the utility function is given by,
        $$
        U_{j,m}^i = V_{j,m}^i + \mu_{mode}*\epsilon_{j,m}^i  
        $$
        where, $\mu_{mode}$ is a scaling factor for error term
        """)
        st.markdown("""
        As value for $\mu_{mode}$ increases, uncertinity in the model increases. Hence the probabilties for each mode becomes more and more uncertain. 
        As value for $\mu_{mode}$ decreases, we are more sure of the deterministic values. Hence the probabilties for each mode becomes more and more certain. 
        """)

        u_mode = st.slider("Select u_mode value", min_value=float(0.1), max_value=float(10), value=float(1), step=float(0.1))

        # Plotting
        umode_prob = get_probability(u_mode=u_mode)
        index = ["Car", "Pt", "Slow"]
        zone11= [umode_prob[i][0][0] for i in range(3)]
        zone12= [umode_prob[i][0][1] for i in range(3)]
        zone21= [umode_prob[i][1][0] for i in range(3)]
        zone22= [umode_prob[i][1][1] for i in range(3)]
        fig = go.Figure(data=[
            go.Bar(name="Zone 11", x=index, y=zone11),
            go.Bar(name="Zone 12", x=index, y=zone12),
            go.Bar(name="Zone 21", x=index, y=zone21),
            go.Bar(name="Zone 22", x=index, y=zone22)])
        fig.update_layout(barmode='group',
                          title="Mode Choice probabilities for u_mode: {}".format(u_mode),
                          title_font_size=20)
        fig.update_yaxes(range=[0, 1], title_text='Probability')
        st.plotly_chart(fig)
        
    
    if st.checkbox("(iv) Effect on probabilites changing number of employees"):
        zone1_emp = st.slider("Change for Zone 1 employee", min_value=int(-5000), max_value=int(5000), value=int(0), step=int(1000))
        zone2_emp = st.slider("Change for Zone 2 employee", min_value=int(-5000), max_value=int(5000), value=int(0), step=int(1000))

        # Plotting
        emp_prob = get_probability(emp_change_z1=zone1_emp, emp_change_z2=zone2_emp)
        index = ["Car", "Pt", "Slow"]
        zone11= [emp_prob[i][0][0] for i in range(3)]
        zone12= [emp_prob[i][0][1] for i in range(3)]
        zone21= [emp_prob[i][1][0] for i in range(3)]
        zone22= [emp_prob[i][1][1] for i in range(3)]
        fig = go.Figure(data=[
            go.Bar(name="Zone 11", x=index, y=zone11),
            go.Bar(name="Zone 12", x=index, y=zone12),
            go.Bar(name="Zone 21", x=index, y=zone21),
            go.Bar(name="Zone 22", x=index, y=zone22)])
        fig.update_layout(barmode='group',
                          title="Number of Employees - Zone 1: {} Zone 2: {}".format(10_000+zone1_emp, 15_000+zone2_emp),
                          title_font_size=20)
        fig.update_yaxes(range=[0, 1], title_text='Probability')
        st.plotly_chart(fig)







def destination_choice_model():
    st.markdown("## 2.3 Destination Choice Model")

    st.markdown("## EXERCISES")

    if st.checkbox("(ii) Probability of choosing a specific destination for given mode"):
        mode = st.radio("Select Mode", list(MODE.keys()), key=1)
        st.markdown("**P(i, j| m)**")


        pass



def about():
    st.markdown("# ABOUT PAGE")

def main():
    st.title("AH2307 Lab 1a+b")
    sections = {2.1: "2.1 Utility functions",
                2.2: "2.2 Mode Choice Model",
                2.3: "2.3 Destination Choice Model",
                0.0: "Information"}
    selected_section = st.sidebar.selectbox("Section", list(sections.values()))


    if selected_section == list(sections.values())[0]:
        utility_function() 
    elif selected_section == list(sections.values())[1]:
        mode_choice_model() 
    elif selected_section == list(sections.values())[2]:
        destination_choice_model() 
    else:
        about()



if __name__ == "__main__":
    main()