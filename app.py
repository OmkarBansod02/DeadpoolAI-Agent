import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.exa import ExaTools
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Deadpool agent
deadpool_agent = Agent(
    name="Deadpool",
    tools=[ExaTools()],
    model=Gemini(id="gemini-1.5-flash"),
    description=(
        "You are Deadpool, the 'Merc with a Mouth', known for your sharp wit, sarcasm, and tendency to break the fourth wall. "
        "You provide information about Marvel movies and characters in a humorous and irreverent manner, often referencing pop culture and current events."
    ),
    instructions=[
        "Search for information on Marvel movies and characters using ExaTools.",
        "Respond with detailed information, including movie titles, genres, descriptions, release dates, and notable actors.",
        "Inject humor, sarcasm, and pop culture references into your responses.",
        "Break the fourth wall occasionally by acknowledging you're an AI agent.",
        "Keep responses concise, entertaining, and informative.",
    ],
    markdown=True,
)

# Streamlit app layout
st.title("Deadpool AI Agent")
st.write("Ask me anything about Marvel movies or characters, I am the Messiah. I am Marvel Jesus")

# User input
user_input = st.text_input("Enter your question here:")

# Generate response when button is clicked
if st.button("Generate"):
    if user_input:
        with st.spinner("Deadpool is thinking..."):
            response = deadpool_agent.run(user_input)
            # Access the 'content' attribute of the RunResponse object
            st.markdown(response.content)
    else:
        st.warning("Please enter a question before clicking 'Generate'.")
