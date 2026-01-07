import streamlit as st
import os
from xai_sdk import Client
from xai_sdk.tools import code_execution, web_search

# ویب پیج کی سیٹنگ
st.set_page_config(page_title="SDN News - Grok AI", page_icon="🤖")
st.title("Grok AI ویب انٹرفیس")

# سائڈ بار میں API Key ان پٹ
with st.sidebar:
    api_key = st.text_input("xAI API Key درج کریں", type="password")
    st.info("یہ ویب سائٹ SDN News کے لیے Grok AI کا استعمال کر رہی ہے۔")

if api_key:
    client = Client(api_key=api_key)
    
    # چیٹ ہسٹری کو محفوظ کرنا
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # پرانی گفتگو دکھانا
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # صارف کا سوال
    if prompt := st.chat_input("آپ کا سوال کیا ہے؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Grok سے جواب حاصل کرنا
        with st.chat_message("assistant"):
            chat = client.chat.create(
                model="grok-4-1-fast-reasoning",
                tools=[web_search(), code_execution()]
            )
            response = chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("براہ کرم سائڈ بار میں اپنی API Key درج کریں۔")
