from web3 import Web3
import os

# Connect to Anryton Blockchain (Example RPC URL, replace with actual Anryton RPC)
rpc_url = os.getenv("RPC_URL", "https://anryton-rpc-url.com")
w3 = Web3(Web3.HTTPProvider(rpc_url))

def send_transaction(encrypted_query, from_address, private_key):
    nonce = w3.eth.getTransactionCount(from_address)
    tx = {
        'nonce': nonce,
        'to': from_address,  # For demo, sending back to self; replace with MOL contract address
        'value': 0,
        'gas': 200000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'data': encrypted_query.encode('utf-8')
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.toHex(tx_hash)
