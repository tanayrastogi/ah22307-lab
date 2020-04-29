# Python Import
import streamlit as st

# Local import
import simulating_choices as sc

def presentation():
    st.markdown("## 2.4 Simulating Choices ")

    if st.checkbox("Show Gumble Distribution?"):    
        # Gumbel Distribution
        mu   = st.slider("Select Mean value", min_value=float(-20), max_value=float(50), value=float(0), step=float(0.1))
        beta = st.slider("Select Variance value", min_value=float(0), max_value=float(10), value=float(1), step=float(0.1))
        
        val, plt = sc.gumbel_distrubution(mu=mu, beta=beta, count=10_00_000, plot=True)
        st.pyplot(plt)
        
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
    if st.checkbox("(ii) Probabilites of each zone given mode"):
        pass
