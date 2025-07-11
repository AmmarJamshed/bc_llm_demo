from web3 import Web3

rpc_url = "https://jsrpc.anryton.com"
w3 = Web3(Web3.HTTPProvider(rpc_url))

def send_transaction(encrypted_query, from_address, private_key):
    nonce = w3.eth.get_transaction_count(from_address)
    tx = {
        'chainId': 130,  # Anryton Mainnet Chain ID
        'nonce': nonce,
        'to': from_address,  # Still sending to self (replace later)
        'value': 0,
        'gas': 21000,
        'gasPrice': w3.to_wei('5', 'gwei'),
        'data': encrypted_query.encode('utf-8')
    }
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    return w3.to_hex(tx_hash)
