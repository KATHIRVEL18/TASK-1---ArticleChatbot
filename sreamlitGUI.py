import streamlit as st
from transformers import pipeline

# Load model
gpt_neo = pipeline('text-generation', model='./gpt_neo_finetuned')

st.title('Article Generator Chatbot')

# User input
user_input = st.text_input("Enter the topic:")

if st.button("Generate Article"):
    output = gpt_neo(user_input, max_length=100, num_return_sequences=1)
    st.write("Generated Article:")
    st.write(output[0]['generated_text'])
