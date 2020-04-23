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
        st.write(pd.DataFrame(utilities[0], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Utility for **PUBLIC TRANSPORT (PT)**")
        st.write(pd.DataFrame(utilities[1], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Utility for **SLOW**")
        st.write(pd.DataFrame(utilities[2], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))

    # Show by Zone and Mode
    st.markdown("## EXCERCISES")
    if st.checkbox("(i)/(ii) Utilities of each mode given zone"):
        orig_zone = st.radio("Select Origin Zone", list(ZONE.keys()))
        dest_zone = st.radio("Select Destination Zone", list(ZONE.keys()))
        mode      = st.radio("Select Mode", list(MODE.keys()))
        utility = get_utility(ZONE[orig_zone], ZONE[dest_zone], MODE[mode])
        st.markdown("### The utility of {} from {} to {} is {}".format(mode, orig_zone, dest_zone, round(utility, 4)))









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
    
    
    
    
    # Show by Zone and Mode
    st.markdown("## EXERCISES")

    if st.checkbox("(ii) Probabilites of each zone given mode"):
        orig_zone = st.radio("Select Origin Zone", list(ZONE.keys()))
        dest_zone = st.radio("Select Destination Zone", list(ZONE.keys()))
        mode      = st.radio("Select Mode", list(MODE.keys()))
        probability = get_probability(ZONE[orig_zone], ZONE[dest_zone], MODE[mode])
        st.markdown("### The probability of {} from {} to {} is {}".format(mode, orig_zone, dest_zone, round(probability, 4)))
    
    if st.checkbox("(iii) Probability of travelling using choosen mode from zone 1 to any destination"):
        mode      = st.radio("Select Mode", list(MODE.keys()))
        zone11    = zone12 = get_probability(ZONE["Zone 1"], ZONE["Zone 1"], MODE[mode])
        zone12    = get_probability(ZONE["Zone 1"], ZONE["Zone 2"], MODE[mode])
        st.markdown("### The probability of using {} from Zone 1 is {}".format(mode, round(zone11*0.5 + zone12*0.5, 4)))

    if st.checkbox("(iv) Effect on probabilites choosing u_mode"):
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
                          title="Bar Chart for each zone for all modes",
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
                          title="Bar Chart for each zone for all modes",
                          title_font_size=20)
        fig.update_yaxes(range=[0, 1], title_text='Probability')
        st.plotly_chart(fig)







def destination_choice_model():
    st.markdown("## 2.3 Destination Choice Model")
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