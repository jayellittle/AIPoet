# from dotenv import load_dotenv
# load_dotenv()

from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

chat_model = ChatOpenAI()
output_parser = StrOutputParser()

st.title("AI Poet")

content = st.text_input("What's the subject of this poem?")

if st.button("Submit"):
    with st.spinner("Writing a poem..."):
        chain = chat_model | output_parser
        result = chain.invoke("Write a poem about the subject delimited in triple backticks. ```" + content + "```")
        st.write(result)
