try:
    import  streamlit as st  # type: ignore[import]
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "Streamlit is not installed. Install it with 'pip install streamlit'."
    ) from e

import datetime

# Page Settings
st.set_page_config(
    page_title="HelpDesk AI",
    page_icon="🤖",
    layout="centered"
)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm HelpDesk AI. How can I help you today?"
        }
    ]

# Rule-Based Responses
def get_response(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"

    elif "password" in text:
        return "To reset your password, click 'Forgot Password' on the login page."

    elif "contact" in text:
        return "You can contact support at support@helpdesk.ai"

    elif "price" in text:
        return "Please visit our pricing page for the latest plans."

    elif "free" in text:
        return "Yes, we offer a free trial."

    elif "bye" in text:
        return "Goodbye! Have a great day. 👋"

    else:
        return "I'm sorry, I didn't understand. Could you rephrase your question?"

# Header
st.title("🤖 HelpDesk AI")
st.caption("Customer Support Chatbot")

# Display Chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat Input
if prompt := st.chat_input("Type your message..."):
    
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = get_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)

# Sidebar
with st.sidebar:
    st.header("Settings")

    if st.button("Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared! How can I help you?"
            }
        ]
        st.rerun()

    st.markdown("---")
    st.write("### Quick Questions")

    quick_questions = [
        "Hello",
        "How do I reset my password?",
        "Is it free?",
        "How do I contact support?"
    ]

    for q in quick_questions:
        if st.button(q):
            response = get_response(q)

            st.session_state.messages.append(
                {"role": "user", "content": q}
            )

            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

            st.rerun()