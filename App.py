import streamlit as st
if 'counter' not in st.session_state:
    st.session_state.counter = 0
MAX_LIMIT = 10
MIN_LIMIT = 0
def decrease():
    if st.session_state.counter > MIN_LIMIT:
        st.session_state.counter -=1
def increase():
    if st.session_state.counter < MAX_LIMIT:
        st.session_state.counter +=1
def reset():
    st.session_state.counter = 0
st.write(f"Value :{st.session_state.counter}")
    
col1,col2,col3 = st.columns(3)
with col1:
    st.button("Increase", on_click=increase)
with col2:
    st.button("Decrease", on_click=decrease)
with col3:
    st.button("reset", on_click=reset)
if st.session_state.counter <= MIN_LIMIT:
    print("You Reached your Minimum Limit")
if st.session_state.counter >= MAX_LIMIT:
    print("You Reached your Maximum Limit")
