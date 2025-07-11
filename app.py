import streamlit as st
from encryption import generate_key, encrypt_message, decrypt_message
from blockchain import send_transaction
from llm import get_llm_response

st.set_page_config(page_title="PrivateGPT on Anryton Blockchain", layout="centered")
st.title("🔒 PrivateGPT: Blockchain-Backed LLM (Anryton Powered) + MetaMask")

query = st.text_area("Enter your Private Query")

# Wallet Connect
st.subheader("🔗 Connect Wallet (MetaMask)")
from_address = st.text_input("Your Wallet Address (from MetaMask)")
private_key = st.text_input("Private Key (for demo only, NEVER do this in production!)", type="password")

if st.button("🔐 Encrypt, Send & Submit Query"):
    if not from_address or not private_key:
        st.error("Wallet address and private key required.")
    else:
        key = generate_key()
        encrypted_query = encrypt_message(query, key)

        try:
            tx_hash = send_transaction(encrypted_query, from_address, private_key)
            st.success(f"Transaction sent to Anryton Blockchain (MOL) ✅\nTx Hash: {tx_hash}")

            # Dummy LLM Response (as before)
            llm_response = get_llm_response(query)
            encrypted_response = encrypt_message(llm_response, key)
            st.session_state.encrypted_response = encrypted_response
            st.session_state.key = key
        except Exception as e:
            st.error(f"Transaction Failed: {e}")

if "encrypted_response" in st.session_state:
    if st.button("🔓 Decrypt Response"):
        decrypted_response = decrypt_message(st.session_state.encrypted_response, st.session_state.key)
        st.success("Response Decrypted Successfully!")
        st.write(decrypted_response)

st.caption("Powered by Anryton Blockchain (MOL) & MetaMask | Demo by Coursemon")
