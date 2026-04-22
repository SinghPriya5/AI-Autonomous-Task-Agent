import streamlit as st
from agent.agent import run_agent

st.title("🔥 AI Autonomous Task Agent")

user_input = st.text_input("Enter your task:")

if st.button("Run Agent"):
    output = run_agent(user_input)
    st.success(output)