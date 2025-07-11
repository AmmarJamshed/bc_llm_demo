#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
from encryption import generate_key, encrypt_message, decrypt_message
from blockchain import store_on_blockchain
from llm import get_llm_response

st.set_page_config(page_title="PrivateGPT on Anryton Blockchain", layout="centered")

st.title("🔒 PrivateGPT: Blockchain-Backed LLM (Anryton Powered)")

# Key Generation
if "key" not in st.session_state:
    st.session_state.key = generate_key()

st.info("Your encryption key is auto-generated for this session (simulating private wallet key).")

query = st.text_area("Enter your Private Query")

if st.button("🔐 Encrypt & Submit Query"):
    encrypted_query = encrypt_message(query, st.session_state.key)
    tx_hash, transaction = store_on_blockchain(encrypted_query)
    st.success("Query Encrypted & Stored on Blockchain (Simulated)")
    
    # Simulate LLM response on encrypted query
    llm_response = get_llm_response(query)
    encrypted_response = encrypt_message(llm_response, st.session_state.key)
    
    st.write("**Transaction Hash:**", tx_hash)
    st.write("**Encrypted Response:**", encrypted_response)
    st.session_state.encrypted_response = encrypted_response

if "encrypted_response" in st.session_state:
    if st.button("🔓 Decrypt Response"):
        decrypted_response = decrypt_message(st.session_state.encrypted_response, st.session_state.key)
        st.success("Response Decrypted Successfully!")
        st.write(decrypted_response)

st.caption("🔗 Powered by Anryton Blockchain (Simulated) | Demo by Coursemon")


# In[ ]:




