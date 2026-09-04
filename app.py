import streamlit as st
from agent import ask_agent

st.set_page_config(
    page_title="CareerMate AI Agent",
    page_icon="🤖",
)

st.title("🤖 CareerMate AI Agent")
st.caption("Your AI/ML career assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask about AI, cloud, RAG, or interview preparation...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("CareerMate is thinking..."):
            try:
                answer = ask_agent(question)
                st.write(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as error:
                st.error(f"Unable to get an answer: {error}")