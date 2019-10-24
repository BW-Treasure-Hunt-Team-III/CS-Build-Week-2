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
    attempts = 0
    while valid_proof(last_proof, proof, difficulty) is False:
        proof = random.randint(0, 950000000)
        attempts += 1

        if attempts >= 8000000:
            return ''

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

    if difficulty is not None:
        leading_zeros = "0" * difficulty
    else:
        leading_zeros = "0" * 6
    
    return guess_hash[0:difficulty] == leading_zeros