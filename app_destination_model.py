# Python Import
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Local Imports
import destination_probability as dp

# Global Constants
MODE = {"Car":0, "PT":1, "Slow":2}
ZONE = {"Zone 1":0, "Zone 2":1}


def presentation():
    st.markdown("## 2.3 Destination Choice Model")
    # Show Probability Matrix
    if st.checkbox("Show Probability Matrixes"):
        st.markdown("Probability of choosing destination given mode and origin")
        probabilities = dp.get_probability()
        st.markdown("Probability for **CAR**")
        st.dataframe(pd.DataFrame(probabilities[0], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Probability for **PUBLIC TRANSPORT (PT)**")
        st.dataframe(pd.DataFrame(probabilities[1], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))
        st.markdown("Probability for **SLOW**")
        st.dataframe(pd.DataFrame(probabilities[2], index=["Zone 1", "Zone 2"], columns=["Zone 1", "Zone 2"]))

    # ------------------------- Write Up for the section ------------------------- #
    # ---------------------------------------------------------------------------- #
    st.markdown("""
    ## Destination Choice Model
    The model calculates the probability of chossing destination given the origin and mode of transport. 
    Hence, we calculate **$Pr(j|i,m)$**, where $m$ is mode and $i$ and $j$ are the origin and destination zones.
    """)  
    st.write("""
    Using the deterministic utility $V_{j,m}^i$ we calculate the the probability of choosing $j$ given $i$ and $m$.
    The utility is given by,  

    $$
    U_{j,m}^i = V_{j,m}^i + \epsilon_{j,m}^i  
    $$
    """)
    st.write("""
    The probability of the choosen destination $j$ given $i$ and $m$ is given by, 

    $$
    Pr(j|i,m) = Pr(U_{j,m}^i > U_{j',m}^i) = \dfrac{\exp^{V_{j,m}^i}}{ \sum_{j'={1,2}} \exp^{V_{j',m}^i} }
    $$
    """)


    # ------------------------------------ EXERCISES ------------------------------#
    # ---------------------------------------------------------------------------- #
    st.markdown("## EXERCISES")
    
    # ------------------------------------ Ques3.a ------------------------------#
    if st.checkbox("(iii [a]) Probabilites of destination given mode and origin zone"):
        orig_zone = st.radio("Select Origin Zone", list(ZONE.keys()))
        dest_zone = st.radio("Select Destination Zone", list(ZONE.keys()))
        mode      = st.radio("Select Mode", list(MODE.keys()), key=1)

        probability = dp.get_probability(origin_zone=ZONE[orig_zone], destination_zone=ZONE[dest_zone], mode=MODE[mode])
        st.markdown("The probability of travelling to **{}** from **{}** using a **{}** is,".format(dest_zone, orig_zone, mode))
        st.markdown("$P(j|i,m)$ = **{}**".format(round(probability, 4)))


    # ------------------------------------ Ques3.b/c ------------------------------#
    if st.checkbox("(iii [b/c]) Effect on probabilites changing number of employees"):
        zone1_emp = st.slider("Change for Zone 1 employee", min_value=int(-5000), max_value=int(10000), value=int(0), step=int(1000))
        zone2_emp = st.slider("Change for Zone 2 employee", min_value=int(-5000), max_value=int(15000), value=int(0), step=int(1000))

        # Plotting
        emp_prob = dp.get_probability(emp_change_z1=zone1_emp, emp_change_z2=zone2_emp)
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

    # ------------------------------------ Ques4 ------------------------------#
    if st.checkbox("(iv) Probability of residing in zone 2 and travelling to chosen zone"):
        # Explanation
        st.write("""
        Using the law of large numbers, 

        $$
        Pr(j|i) = \sum_{m={1,2,3}} Pr(j|i,m)*P(m)
        $$

        where, $P(j)$ is 1/3 for each zone, $i = 1$
        """)
        
        # Answer
        dest_zone = st.radio("Select destination zone", list(ZONE.keys()), key=2)
        car  = dp.get_probability(origin_zone=ZONE["Zone 1"], destination_zone=ZONE[dest_zone], mode=0)
        pt   = dp.get_probability(origin_zone=ZONE["Zone 1"], destination_zone=ZONE[dest_zone], mode=1)
        slow = dp.get_probability(origin_zone=ZONE["Zone 1"], destination_zone=ZONE[dest_zone], mode=1)

        st.markdown("The probability of travelling from **Zone 2** to **{}** is,".format(dest_zone))
        st.markdown("$P(j|i=2)$ = **{}**".format(round(car*(1/3) + pt*(1/3) + slow*(1/3), 4)))
