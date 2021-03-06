# Python Import
import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.graph_objects as go

# Local import
import simulating_choices as sc

# Global Constants
MODE = {"Car":0, "PT":1, "Slow":2}
ZONE = {"Zone 1":0, "Zone 2":1}

def presentation():
    st.markdown("## 2.4 Simulating Choices ")

    # if st.checkbox("Show Gumble Distribution?"):    
    #     # Gumbel Distribution
    #     mu   = st.slider("Select Mean value", min_value=float(-20), max_value=float(50), value=float(0), step=float(0.1))
    #     beta = st.slider("Select Variance value", min_value=float(0), max_value=float(10), value=float(1), step=float(0.1))
        
    #     val, plt = sc.gumbel_distrubution(mu=mu, beta=beta, count=10_00_000, plot=True)
    #     st.pyplot(plt)
        
    # ------------------------- Write Up for the section ------------------------- #
    # ---------------------------------------------------------------------------- #
    st.markdown("""
    Here we will be simulating **Mode Choice Model** when origin is **Zone 1** and destination is **Zone 2**.
    Remember that the choosen alternative according to the MNL model is the utility maximizing alternative, 
    i.e, the alternative $m$ for which: 
    """)
    st.write("""
    $$
    U_{j,m}^i \gt U_{j,m'}^i \\thinspace \\forall m' \in \{car, pt, slow\}
    $$
    or equally,
    $$
    m = \\max_{m' \in \{car, pt, slow\}} U_{j,m'}^i
    $$
    where,  
    $$
    U_{j,m'}^i = V_{j,m'}^i + \epsilon_{j,m'}^i  
    $$
    and $\epsilon_{j,m'}^i$ is I.I.D Gumble distributed error term representing uncertinity. 
    """)
    st.markdown("""
    One can thus simulate a choice by simulating draws of  for respectively alternative 
    and making a choice according to given equation.
    """)

    # ------------------------------------ EXERCISES ------------------------------#
    # ---------------------------------------------------------------------------- #
    st.markdown("## EXERCISES")

    # ------------------------------------ Ques2 ------------------------------#
    if st.checkbox("(i) Simulating choices for each mode with gumbel distribution"):
        # Number of samples
        sample_count = st.number_input("Number of samples",
                                        min_value=int(1000),
                                        max_value=int(50_00_000),
                                        value=int(10_00_000),
                                        step=int(1000))
        # Gumbel Distribution
        mu   = st.slider("Select Mean value",
                        min_value=float(-20), max_value=float(50), value=float(0), step=float(0.1))
        beta = st.slider("Select Variance value",
                        min_value=float(0), max_value=float(10), value=float(1), step=float(0.1))
        if st.checkbox("Plot distribution?"):
            val, plot_gumbel = sc.gumbel_distrubution(mu=mu, beta=beta, count=10_00_000, plot=True)
            st.pyplot(plot_gumbel)
        
        # Origin and Destination
        orig_zone = st.radio("Select Origin Zone", list(ZONE.keys()))
        dest_zone = st.radio("Select Destination Zone", list(ZONE.keys()))

        # Get values
        with st.spinner("Sampling values"):
            max_U, max_U_index, count_dict = sc.model_sampling(num_samples=sample_count,
                                                    mu=mu,
                                                    beta=beta,
                                                    origin_zone=ZONE[orig_zone],
                                                    destination_zone=ZONE[dest_zone])
            st.success("Done simulating for {} samples!".format(sample_count))
        

        st.markdown("### Number of times the mode is selected from {} samples".format(sample_count))
        valu = np.array(list(count_dict.values())).reshape(3,1)
        prob = np.divide(valu, sample_count).reshape(3,1)
        data = np.hstack((valu, prob)).reshape(3,2)
        df = pd.DataFrame(data, index=list(MODE.keys()), columns=["COUNT", "PROBABILITY"])
        st.table(df)

        # Plot
        fig = go.Figure(data=[go.Histogram(x=max_U,
                                            nbinsx=30)])
        fig.update_layout(barmode='group',
                        title="Distrubution of max_U for {} samples".format(sample_count),
                        title_font_size=20)
        st.plotly_chart(fig)