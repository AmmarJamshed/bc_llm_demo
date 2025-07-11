#!/usr/bin/env python
# coding: utf-8

# In[2]:


import hashlib
import json
import time

# Simulate Blockchain Storage (In-Memory)
blockchain_storage = []

def store_on_blockchain(encrypted_query):
    tx_hash = hashlib.sha256(encrypted_query.encode()).hexdigest()
    transaction = {
        "tx_hash": tx_hash,
        "encrypted_query": encrypted_query,
        "timestamp": time.time()
    }
    blockchain_storage.append(transaction)
    return tx_hash, transaction

