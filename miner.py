import hashlib
import requests

import sys


from timeit import default_timer as timer

import random


def proof_of_work(last_proof, difficulty):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    - Note:  We are adding the hash of the last proof to a number/nonce for the new proof
    """

    start = timer()

    print("Searching for next proof")
    proof = 0
    
    while valid_proof(last_proof, proof, difficulty) is False:
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_proof, proof, difficulty):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the proof?
    IE:  last_hash: ...AE9123456, new hash 123456888...
    """

    #last_hash = hashlib.sha256(f'{last_proof}'.encode()).hexdigest()

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    leading_zeros = "0" * difficulty
    
    return guess_hash[0:difficulty] == leading_zeros


if __name__ == '__main__':


    coins_mined = 0

    # Run forever until interrupted
    for i in range(0, 50):
        # Get the last proof from the server
        headers = {'Content-Type': 'application/json', 'Authorization': 'Token 636d48a60803e8f600139e8a47d731a28141474b'}  

        r = requests.get(url="https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof", headers=headers)
        data = r.json()
        new_proof = proof_of_work(data.get('proof'), data.get('difficulty'))
        

        post_data = {"proof": new_proof}


        r = requests.post(url="https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/", headers = headers, json=post_data)
        data = r.json()

        print(data)

        # if data.get('message') == 'New Block Forged':
        #     coins_mined += 1
        #     print("Total coins mined: " + str(coins_mined))
        # else:
        #     print(data.get('message'))