# Python Imports
import streamlit as st
import pandas as pd

# Local Imports
import app_utility_function as app_ut
import app_mode_choice as app_md
import app_destination_model as app_dm
import app_simulating_choice as app_sc

def utility_function():
    app_ut.presentation()

def mode_choice_model():
    app_md.presentation()

def destination_choice_model():
    app_dm.presentation()

def simulating_choices():
    app_sc.presentation()

def about():
    st.markdown("# ABOUT PAGE")





def main():
    st.title("Lab 1 - Multinomial and Nested Logit")
    sections = {2.1: "2.1 Utility functions",
                2.2: "2.2 Mode Choice Model",
                2.3: "2.3 Destination Choice Model",
                2.4: "2.4 Simulating Choices",
                0.0: "About"}

    # Side bar
    st.sidebar.title("AH2307 Lab-1")
    selected_section = st.sidebar.selectbox("Section", list(sections.values()))

    if selected_section == list(sections.values())[0]:
        utility_function() 
    elif selected_section == list(sections.values())[1]:
        mode_choice_model() 
    elif selected_section == list(sections.values())[2]:
        destination_choice_model() 
    elif selected_section == list(sections.values())[3]:
        simulating_choices() 
    else:
        about()




if __name__ == "__main__":
    main()