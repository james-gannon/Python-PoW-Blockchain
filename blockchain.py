# Create Blockchain

# Import libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify # (Falsk and jsonify classes from flask library)

# Blockchain Logic

class Blockchain:
    
    # Initialization method
    def __init__(self): # will refer to the object we create once the class is made
        self.chain = [] # list containing the chain
        self.create_block(proof = 1, previous_hash = '0') # common practice is to choose prev hash of '0' for genesis block

    # Create block method
    def create_block(self, proof, previous_hash): # mining will give us the proof based on the defined PoW
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash} # dictionary
        self.chain.append(block)
        return block
    
    # Get prev. block method
    def get_previous_block(self):
        return self.chain[-1] # the last block of the chain
    
    # PoW method
    def proof_of_work(self, previous_proof): # Number that is hard to find, and easy to verify
        new_proof = 1 # Solving the problem (proof) with trial and error approach
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() # '+', you will have the same proof every 2 blocks, which is symmetrical. '-', gives non-symmetric
            # .encode() is just for format purposes so that SHA256 will accept this operation
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    # Check if each block has correct PoW, previous_hash in each block, equals the hash in the previous block
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False # this would make our chain invalid
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest() # '+', you will have the same proof every 2 blocks, which is symmetrical. '-', gives non-symmetric
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
#Blockchain Mining

# Creating a web app
app = Flask(__name__)
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        
# Creating a blockchain
blockchain = Blockchain()

# Mining a new block
@app.route('/mine_block', methods = ['GET']) # route decorator
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congrats! You just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200 # return HTTP request code for success (200 = OK)

# Getting the full blockchain displayed
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

#Check chain validity
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    valid_or_not = blockchain.is_chain_valid(blockchain.chain)
    response = {'valid?': valid_or_not}
    return jsonify(response), 200

# Running the app
app.run(host = '0.0.0.0', port = 5000)
























































